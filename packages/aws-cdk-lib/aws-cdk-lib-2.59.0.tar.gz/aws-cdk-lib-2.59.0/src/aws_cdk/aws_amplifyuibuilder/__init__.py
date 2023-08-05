'''
# AWS::AmplifyUIBuilder Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_amplifyuibuilder as amplifyuibuilder
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AmplifyUIBuilder construct libraries](https://constructs.dev/search?q=amplifyuibuilder)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AmplifyUIBuilder resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AmplifyUIBuilder.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AmplifyUIBuilder](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AmplifyUIBuilder.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnComponent(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent",
):
    '''A CloudFormation ``AWS::AmplifyUIBuilder::Component``.

    The AWS::AmplifyUIBuilder::Component resource specifies a component within an Amplify app. A component is a user interface (UI) element that you can customize. Use ``ComponentChild`` to configure an instance of a ``Component`` . A ``ComponentChild`` instance inherits the configuration of the main ``Component`` .

    :cloudformationResource: AWS::AmplifyUIBuilder::Component
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
        
        # component_child_property_: amplifyuibuilder.CfnComponent.ComponentChildProperty
        # component_property_property_: amplifyuibuilder.CfnComponent.ComponentPropertyProperty
        # overrides: Any
        # predicate_property_: amplifyuibuilder.CfnComponent.PredicateProperty
        
        cfn_component = amplifyuibuilder.CfnComponent(self, "MyCfnComponent",
            binding_properties={
                "binding_properties_key": amplifyuibuilder.CfnComponent.ComponentBindingPropertiesValueProperty(
                    binding_properties=amplifyuibuilder.CfnComponent.ComponentBindingPropertiesValuePropertiesProperty(
                        bucket="bucket",
                        default_value="defaultValue",
                        field="field",
                        key="key",
                        model="model",
                        predicates=[amplifyuibuilder.CfnComponent.PredicateProperty(
                            and=[predicate_property_],
                            field="field",
                            operand="operand",
                            operator="operator",
                            or=[predicate_property_]
                        )],
                        user_attribute="userAttribute"
                    ),
                    default_value="defaultValue",
                    type="type"
                )
            },
            component_type="componentType",
            name="name",
            overrides=overrides,
            properties={
                "properties_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                        property="property",
        
                        # the properties below are optional
                        field="field"
                    ),
                    bindings={
                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                            element="element",
                            property="property"
                        )
                    },
                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                        property="property",
        
                        # the properties below are optional
                        field="field"
                    ),
                    component_name="componentName",
                    concat=[component_property_property_],
                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                        else=component_property_property_,
                        field="field",
                        operand="operand",
                        operand_type="operandType",
                        operator="operator",
                        property="property",
                        then=component_property_property_
                    ),
                    configured=False,
                    default_value="defaultValue",
                    event="event",
                    imported_value="importedValue",
                    model="model",
                    property="property",
                    type="type",
                    user_attribute="userAttribute",
                    value="value"
                )
            },
            variants=[amplifyuibuilder.CfnComponent.ComponentVariantProperty(
                overrides=overrides,
                variant_values={
                    "variant_values_key": "variantValues"
                }
            )],
        
            # the properties below are optional
            children=[amplifyuibuilder.CfnComponent.ComponentChildProperty(
                component_type="componentType",
                name="name",
                properties={
                    "properties_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
        
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
        
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    )
                },
        
                # the properties below are optional
                children=[component_child_property_],
                events={
                    "events_key": amplifyuibuilder.CfnComponent.ComponentEventProperty(
                        action="action",
                        parameters=amplifyuibuilder.CfnComponent.ActionParametersProperty(
                            anchor=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            ),
                            fields={
                                "fields_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
        
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
        
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                )
                            },
                            global=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            ),
                            id=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            ),
                            model="model",
                            state=amplifyuibuilder.CfnComponent.MutationActionSetStateParameterProperty(
                                component_name="componentName",
                                property="property",
                                set=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
        
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
        
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                )
                            ),
                            target=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            ),
                            type=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            ),
                            url=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            )
                        )
                    )
                }
            )],
            collection_properties={
                "collection_properties_key": amplifyuibuilder.CfnComponent.ComponentDataConfigurationProperty(
                    model="model",
        
                    # the properties below are optional
                    identifiers=["identifiers"],
                    predicate=amplifyuibuilder.CfnComponent.PredicateProperty(
                        and=[predicate_property_],
                        field="field",
                        operand="operand",
                        operator="operator",
                        or=[predicate_property_]
                    ),
                    sort=[amplifyuibuilder.CfnComponent.SortPropertyProperty(
                        direction="direction",
                        field="field"
                    )]
                )
            },
            events={
                "events_key": amplifyuibuilder.CfnComponent.ComponentEventProperty(
                    action="action",
                    parameters=amplifyuibuilder.CfnComponent.ActionParametersProperty(
                        anchor=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        fields={
                            "fields_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            )
                        },
                        global=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        id=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        model="model",
                        state=amplifyuibuilder.CfnComponent.MutationActionSetStateParameterProperty(
                            component_name="componentName",
                            property="property",
                            set=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
        
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            )
                        ),
                        target=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        type=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        url=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
        
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        )
                    )
                )
            },
            schema_version="schemaVersion",
            source_id="sourceId",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        binding_properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnComponent.ComponentBindingPropertiesValueProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        component_type: builtins.str,
        name: builtins.str,
        overrides: typing.Any,
        properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        variants: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnComponent.ComponentVariantProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        children: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnComponent.ComponentChildProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        collection_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnComponent.ComponentDataConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnComponent.ComponentEventProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        schema_version: typing.Optional[builtins.str] = None,
        source_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::AmplifyUIBuilder::Component``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param binding_properties: The information to connect a component's properties to data at runtime. You can't specify ``tags`` as a valid property for ``bindingProperties`` .
        :param component_type: The type of the component. This can be an Amplify custom UI component or another custom component.
        :param name: The name of the component.
        :param overrides: Describes the component's properties that can be overriden in a customized instance of the component. You can't specify ``tags`` as a valid property for ``overrides`` .
        :param properties: Describes the component's properties. You can't specify ``tags`` as a valid property for ``properties`` .
        :param variants: A list of the component's variants. A variant is a unique style configuration of a main component.
        :param children: A list of the component's ``ComponentChild`` instances.
        :param collection_properties: The data binding configuration for the component's properties. Use this for a collection component. You can't specify ``tags`` as a valid property for ``collectionProperties`` .
        :param events: Describes the events that can be raised on the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
        :param schema_version: The schema version of the component when it was imported.
        :param source_id: The unique ID of the component in its original source system, such as Figma.
        :param tags: One or more key-value pairs to use when tagging the component.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd7799829199faf127a94fa77781fc238076f764c5a29e3192b18302477d99ad)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnComponentProps(
            binding_properties=binding_properties,
            component_type=component_type,
            name=name,
            overrides=overrides,
            properties=properties,
            variants=variants,
            children=children,
            collection_properties=collection_properties,
            events=events,
            schema_version=schema_version,
            source_id=source_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a4071d72b1c192773d27cf1393fcd31a209b8da1710b4cc3887aaa640711a2b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5845dbb422dcf82315243e4c81979c1db599d6f4e807c7e8d29cce12a0123aba)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAppId")
    def attr_app_id(self) -> builtins.str:
        '''The unique ID for the Amplify app.

        :cloudformationAttribute: AppId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentName")
    def attr_environment_name(self) -> builtins.str:
        '''The name of the backend environment that is a part of the Amplify app.

        :cloudformationAttribute: EnvironmentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentName"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique ID of the component.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''One or more key-value pairs to use when tagging the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="bindingProperties")
    def binding_properties(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentBindingPropertiesValueProperty", _IResolvable_da3f097b]]]:
        '''The information to connect a component's properties to data at runtime.

        You can't specify ``tags`` as a valid property for ``bindingProperties`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-bindingproperties
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentBindingPropertiesValueProperty", _IResolvable_da3f097b]]], jsii.get(self, "bindingProperties"))

    @binding_properties.setter
    def binding_properties(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentBindingPropertiesValueProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4318ac16b5fec407f318eecf547fbef09f6a25d44eee663a0eb2d9d4cfb515c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bindingProperties", value)

    @builtins.property
    @jsii.member(jsii_name="componentType")
    def component_type(self) -> builtins.str:
        '''The type of the component.

        This can be an Amplify custom UI component or another custom component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-componenttype
        '''
        return typing.cast(builtins.str, jsii.get(self, "componentType"))

    @component_type.setter
    def component_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d75568dbcc6cfcf6d654bc9d347cea6e2a04e9fed153e3f59a35fd309d097273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "componentType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d390004d0f30759542ef28ada1804bcce6e8abbebac682bdb562339425f06133)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="overrides")
    def overrides(self) -> typing.Any:
        '''Describes the component's properties that can be overriden in a customized instance of the component.

        You can't specify ``tags`` as a valid property for ``overrides`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-overrides
        '''
        return typing.cast(typing.Any, jsii.get(self, "overrides"))

    @overrides.setter
    def overrides(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0df3bcfbc7a5f3b8c1c149ff6cbac150b1f0b40f2b39df29eaf014b9a94c7083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrides", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]]:
        '''Describes the component's properties.

        You can't specify ``tags`` as a valid property for ``properties`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-properties
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]], jsii.get(self, "properties"))

    @properties.setter
    def properties(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__996d9ae7924c5b47d79b0dc8a0bdd64fe013219ccbe4230a2423b7e9ad5aba37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="variants")
    def variants(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.ComponentVariantProperty", _IResolvable_da3f097b]]]:
        '''A list of the component's variants.

        A variant is a unique style configuration of a main component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-variants
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.ComponentVariantProperty", _IResolvable_da3f097b]]], jsii.get(self, "variants"))

    @variants.setter
    def variants(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.ComponentVariantProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21622fc70206995803294c972e78d130850c0e1dde7f836f2646dd47d873fc48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variants", value)

    @builtins.property
    @jsii.member(jsii_name="children")
    def children(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.ComponentChildProperty", _IResolvable_da3f097b]]]]:
        '''A list of the component's ``ComponentChild`` instances.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-children
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.ComponentChildProperty", _IResolvable_da3f097b]]]], jsii.get(self, "children"))

    @children.setter
    def children(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.ComponentChildProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc8d6f7afd78df5a6542a7697bbb32d8d2c9e5a18e80e3386de082f4e2b7071)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "children", value)

    @builtins.property
    @jsii.member(jsii_name="collectionProperties")
    def collection_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentDataConfigurationProperty", _IResolvable_da3f097b]]]]:
        '''The data binding configuration for the component's properties.

        Use this for a collection component. You can't specify ``tags`` as a valid property for ``collectionProperties`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-collectionproperties
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentDataConfigurationProperty", _IResolvable_da3f097b]]]], jsii.get(self, "collectionProperties"))

    @collection_properties.setter
    def collection_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentDataConfigurationProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ccd617dfcaf796edb26a70160a96d7ac3771afa99ba8a4500e7927f724ee8d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectionProperties", value)

    @builtins.property
    @jsii.member(jsii_name="events")
    def events(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentEventProperty", _IResolvable_da3f097b]]]]:
        '''Describes the events that can be raised on the component.

        Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-events
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentEventProperty", _IResolvable_da3f097b]]]], jsii.get(self, "events"))

    @events.setter
    def events(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentEventProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__867f4afaa52290132593733e3be70d110a540505523ee1a4b0bea23f5a059f8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "events", value)

    @builtins.property
    @jsii.member(jsii_name="schemaVersion")
    def schema_version(self) -> typing.Optional[builtins.str]:
        '''The schema version of the component when it was imported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-schemaversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaVersion"))

    @schema_version.setter
    def schema_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cce35ca7f734518c2d5b6c459ad169208cc7c4b0e7c4955205c3b6e4bdc8f484)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="sourceId")
    def source_id(self) -> typing.Optional[builtins.str]:
        '''The unique ID of the component in its original source system, such as Figma.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-sourceid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceId"))

    @source_id.setter
    def source_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1265b5d410f7cdf2344a649e0fe6921e9ffd6d7c60569ba0b37eedfeea753d74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.ActionParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "anchor": "anchor",
            "fields": "fields",
            "global_": "global",
            "id": "id",
            "model": "model",
            "state": "state",
            "target": "target",
            "type": "type",
            "url": "url",
        },
    )
    class ActionParametersProperty:
        def __init__(
            self,
            *,
            anchor: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            global_: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            id: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            model: typing.Optional[builtins.str] = None,
            state: typing.Optional[typing.Union[typing.Union["CfnComponent.MutationActionSetStateParameterProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            target: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            type: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            url: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``ActionParameters`` property specifies the event action configuration for an element of a ``Component`` or ``ComponentChild`` .

            Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components. ``ActionParameters`` defines the action that is performed when an event occurs on the component.

            :param anchor: The HTML anchor link to the location to open. Specify this value for a navigation action.
            :param fields: A dictionary of key-value pairs mapping Amplify Studio properties to fields in a data model. Use when the action performs an operation on an Amplify DataStore model.
            :param global_: Specifies whether the user should be signed out globally. Specify this value for an auth sign out action.
            :param id: The unique ID of the component that the ``ActionParameters`` apply to.
            :param model: The name of the data model. Use when the action performs an operation on an Amplify DataStore model.
            :param state: A key-value pair that specifies the state property name and its initial value.
            :param target: The element within the same component to modify when the action occurs.
            :param type: The type of navigation action. Valid values are ``url`` and ``anchor`` . This value is required for a navigation action.
            :param url: The URL to the location to open. Specify this value for a navigation action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # component_property_property_: amplifyuibuilder.CfnComponent.ComponentPropertyProperty
                
                action_parameters_property = amplifyuibuilder.CfnComponent.ActionParametersProperty(
                    anchor=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    ),
                    fields={
                        "fields_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        )
                    },
                    global=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    ),
                    id=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    ),
                    model="model",
                    state=amplifyuibuilder.CfnComponent.MutationActionSetStateParameterProperty(
                        component_name="componentName",
                        property="property",
                        set=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        )
                    ),
                    target=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    ),
                    type=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    ),
                    url=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__396df9c0159ef2683a2d199aa0e6b6baece439a466a700800ddc5e140dd124b1)
                check_type(argname="argument anchor", value=anchor, expected_type=type_hints["anchor"])
                check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
                check_type(argname="argument global_", value=global_, expected_type=type_hints["global_"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument model", value=model, expected_type=type_hints["model"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if anchor is not None:
                self._values["anchor"] = anchor
            if fields is not None:
                self._values["fields"] = fields
            if global_ is not None:
                self._values["global_"] = global_
            if id is not None:
                self._values["id"] = id
            if model is not None:
                self._values["model"] = model
            if state is not None:
                self._values["state"] = state
            if target is not None:
                self._values["target"] = target
            if type is not None:
                self._values["type"] = type
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def anchor(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]:
            '''The HTML anchor link to the location to open.

            Specify this value for a navigation action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-anchor
            '''
            result = self._values.get("anchor")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def fields(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]]]:
            '''A dictionary of key-value pairs mapping Amplify Studio properties to fields in a data model.

            Use when the action performs an operation on an Amplify DataStore model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-fields
            '''
            result = self._values.get("fields")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def global_(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]:
            '''Specifies whether the user should be signed out globally.

            Specify this value for an auth sign out action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-global
            '''
            result = self._values.get("global_")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def id(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]:
            '''The unique ID of the component that the ``ActionParameters`` apply to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def model(self) -> typing.Optional[builtins.str]:
            '''The name of the data model.

            Use when the action performs an operation on an Amplify DataStore model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-model
            '''
            result = self._values.get("model")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def state(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.MutationActionSetStateParameterProperty", _IResolvable_da3f097b]]:
            '''A key-value pair that specifies the state property name and its initial value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.MutationActionSetStateParameterProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def target(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]:
            '''The element within the same component to modify when the action occurs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def type(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]:
            '''The type of navigation action.

            Valid values are ``url`` and ``anchor`` . This value is required for a navigation action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def url(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]:
            '''The URL to the location to open.

            Specify this value for a navigation action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.ComponentBindingPropertiesValuePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "default_value": "defaultValue",
            "field": "field",
            "key": "key",
            "model": "model",
            "predicates": "predicates",
            "user_attribute": "userAttribute",
        },
    )
    class ComponentBindingPropertiesValuePropertiesProperty:
        def __init__(
            self,
            *,
            bucket: typing.Optional[builtins.str] = None,
            default_value: typing.Optional[builtins.str] = None,
            field: typing.Optional[builtins.str] = None,
            key: typing.Optional[builtins.str] = None,
            model: typing.Optional[builtins.str] = None,
            predicates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnComponent.PredicateProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            user_attribute: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``ComponentBindingPropertiesValueProperties`` property specifies the data binding configuration for a specific property using data stored in AWS .

            For AWS connected properties, you can bind a property to data stored in an Amazon S3 bucket, an Amplify DataStore model or an authenticated user attribute.

            :param bucket: An Amazon S3 bucket.
            :param default_value: The default value to assign to the property.
            :param field: The field to bind the data to.
            :param key: The storage key for an Amazon S3 bucket.
            :param model: An Amplify DataStore model.
            :param predicates: A list of predicates for binding a component's properties to data.
            :param user_attribute: An authenticated user attribute.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # predicate_property_: amplifyuibuilder.CfnComponent.PredicateProperty
                
                component_binding_properties_value_properties_property = amplifyuibuilder.CfnComponent.ComponentBindingPropertiesValuePropertiesProperty(
                    bucket="bucket",
                    default_value="defaultValue",
                    field="field",
                    key="key",
                    model="model",
                    predicates=[amplifyuibuilder.CfnComponent.PredicateProperty(
                        and=[predicate_property_],
                        field="field",
                        operand="operand",
                        operator="operator",
                        or=[predicate_property_]
                    )],
                    user_attribute="userAttribute"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__81ff632b19dd9fd8d12fdc9b6929e5e551d79797cb14dd1ca0cf7644998a657c)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument model", value=model, expected_type=type_hints["model"])
                check_type(argname="argument predicates", value=predicates, expected_type=type_hints["predicates"])
                check_type(argname="argument user_attribute", value=user_attribute, expected_type=type_hints["user_attribute"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket is not None:
                self._values["bucket"] = bucket
            if default_value is not None:
                self._values["default_value"] = default_value
            if field is not None:
                self._values["field"] = field
            if key is not None:
                self._values["key"] = key
            if model is not None:
                self._values["model"] = model
            if predicates is not None:
                self._values["predicates"] = predicates
            if user_attribute is not None:
                self._values["user_attribute"] = user_attribute

        @builtins.property
        def bucket(self) -> typing.Optional[builtins.str]:
            '''An Amazon S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-bucket
            '''
            result = self._values.get("bucket")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''The default value to assign to the property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field(self) -> typing.Optional[builtins.str]:
            '''The field to bind the data to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-field
            '''
            result = self._values.get("field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The storage key for an Amazon S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def model(self) -> typing.Optional[builtins.str]:
            '''An Amplify DataStore model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-model
            '''
            result = self._values.get("model")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def predicates(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.PredicateProperty", _IResolvable_da3f097b]]]]:
            '''A list of predicates for binding a component's properties to data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-predicates
            '''
            result = self._values.get("predicates")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.PredicateProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def user_attribute(self) -> typing.Optional[builtins.str]:
            '''An authenticated user attribute.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-userattribute
            '''
            result = self._values.get("user_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentBindingPropertiesValuePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.ComponentBindingPropertiesValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "binding_properties": "bindingProperties",
            "default_value": "defaultValue",
            "type": "type",
        },
    )
    class ComponentBindingPropertiesValueProperty:
        def __init__(
            self,
            *,
            binding_properties: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentBindingPropertiesValuePropertiesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            default_value: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``ComponentBindingPropertiesValue`` property specifies the data binding configuration for a component at runtime.

            You can use ``ComponentBindingPropertiesValue`` to add exposed properties to a component to allow different values to be entered when a component is reused in different places in an app.

            :param binding_properties: Describes the properties to customize with data at runtime.
            :param default_value: The default value of the property.
            :param type: The property type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # predicate_property_: amplifyuibuilder.CfnComponent.PredicateProperty
                
                component_binding_properties_value_property = amplifyuibuilder.CfnComponent.ComponentBindingPropertiesValueProperty(
                    binding_properties=amplifyuibuilder.CfnComponent.ComponentBindingPropertiesValuePropertiesProperty(
                        bucket="bucket",
                        default_value="defaultValue",
                        field="field",
                        key="key",
                        model="model",
                        predicates=[amplifyuibuilder.CfnComponent.PredicateProperty(
                            and=[predicate_property_],
                            field="field",
                            operand="operand",
                            operator="operator",
                            or=[predicate_property_]
                        )],
                        user_attribute="userAttribute"
                    ),
                    default_value="defaultValue",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff7030ae0aef39d7f52ec52503b8ffe4b3b2f9eab3ec5a0b307d62df215fac00)
                check_type(argname="argument binding_properties", value=binding_properties, expected_type=type_hints["binding_properties"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if binding_properties is not None:
                self._values["binding_properties"] = binding_properties
            if default_value is not None:
                self._values["default_value"] = default_value
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def binding_properties(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentBindingPropertiesValuePropertiesProperty", _IResolvable_da3f097b]]:
            '''Describes the properties to customize with data at runtime.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalue.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalue-bindingproperties
            '''
            result = self._values.get("binding_properties")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentBindingPropertiesValuePropertiesProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''The default value of the property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalue.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalue-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The property type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalue.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalue-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentBindingPropertiesValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.ComponentChildProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_type": "componentType",
            "name": "name",
            "properties": "properties",
            "children": "children",
            "events": "events",
        },
    )
    class ComponentChildProperty:
        def __init__(
            self,
            *,
            component_type: builtins.str,
            name: builtins.str,
            properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
            children: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnComponent.ComponentChildProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnComponent.ComponentEventProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The ``ComponentChild`` property specifies a nested UI configuration within a parent ``Component`` .

            :param component_type: The type of the child component.
            :param name: The name of the child component.
            :param properties: Describes the properties of the child component. You can't specify ``tags`` as a valid property for ``properties`` .
            :param children: The list of ``ComponentChild`` instances for this component.
            :param events: Describes the events that can be raised on the child component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # component_child_property_: amplifyuibuilder.CfnComponent.ComponentChildProperty
                # component_property_property_: amplifyuibuilder.CfnComponent.ComponentPropertyProperty
                
                component_child_property = amplifyuibuilder.CfnComponent.ComponentChildProperty(
                    component_type="componentType",
                    name="name",
                    properties={
                        "properties_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        )
                    },
                
                    # the properties below are optional
                    children=[amplifyuibuilder.CfnComponent.ComponentChildProperty(
                        component_type="componentType",
                        name="name",
                        properties={
                            "properties_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
                
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
                
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            )
                        },
                
                        # the properties below are optional
                        children=[component_child_property_],
                        events={
                            "events_key": amplifyuibuilder.CfnComponent.ComponentEventProperty(
                                action="action",
                                parameters=amplifyuibuilder.CfnComponent.ActionParametersProperty(
                                    anchor=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        bindings={
                                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                element="element",
                                                property="property"
                                            )
                                        },
                                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        component_name="componentName",
                                        concat=[component_property_property_],
                                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                            else=component_property_property_,
                                            field="field",
                                            operand="operand",
                                            operand_type="operandType",
                                            operator="operator",
                                            property="property",
                                            then=component_property_property_
                                        ),
                                        configured=False,
                                        default_value="defaultValue",
                                        event="event",
                                        imported_value="importedValue",
                                        model="model",
                                        property="property",
                                        type="type",
                                        user_attribute="userAttribute",
                                        value="value"
                                    ),
                                    fields={
                                        "fields_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                                property="property",
                
                                                # the properties below are optional
                                                field="field"
                                            ),
                                            bindings={
                                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                    element="element",
                                                    property="property"
                                                )
                                            },
                                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                                property="property",
                
                                                # the properties below are optional
                                                field="field"
                                            ),
                                            component_name="componentName",
                                            concat=[component_property_property_],
                                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                                else=component_property_property_,
                                                field="field",
                                                operand="operand",
                                                operand_type="operandType",
                                                operator="operator",
                                                property="property",
                                                then=component_property_property_
                                            ),
                                            configured=False,
                                            default_value="defaultValue",
                                            event="event",
                                            imported_value="importedValue",
                                            model="model",
                                            property="property",
                                            type="type",
                                            user_attribute="userAttribute",
                                            value="value"
                                        )
                                    },
                                    global=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        bindings={
                                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                element="element",
                                                property="property"
                                            )
                                        },
                                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        component_name="componentName",
                                        concat=[component_property_property_],
                                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                            else=component_property_property_,
                                            field="field",
                                            operand="operand",
                                            operand_type="operandType",
                                            operator="operator",
                                            property="property",
                                            then=component_property_property_
                                        ),
                                        configured=False,
                                        default_value="defaultValue",
                                        event="event",
                                        imported_value="importedValue",
                                        model="model",
                                        property="property",
                                        type="type",
                                        user_attribute="userAttribute",
                                        value="value"
                                    ),
                                    id=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        bindings={
                                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                element="element",
                                                property="property"
                                            )
                                        },
                                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        component_name="componentName",
                                        concat=[component_property_property_],
                                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                            else=component_property_property_,
                                            field="field",
                                            operand="operand",
                                            operand_type="operandType",
                                            operator="operator",
                                            property="property",
                                            then=component_property_property_
                                        ),
                                        configured=False,
                                        default_value="defaultValue",
                                        event="event",
                                        imported_value="importedValue",
                                        model="model",
                                        property="property",
                                        type="type",
                                        user_attribute="userAttribute",
                                        value="value"
                                    ),
                                    model="model",
                                    state=amplifyuibuilder.CfnComponent.MutationActionSetStateParameterProperty(
                                        component_name="componentName",
                                        property="property",
                                        set=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                                property="property",
                
                                                # the properties below are optional
                                                field="field"
                                            ),
                                            bindings={
                                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                    element="element",
                                                    property="property"
                                                )
                                            },
                                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                                property="property",
                
                                                # the properties below are optional
                                                field="field"
                                            ),
                                            component_name="componentName",
                                            concat=[component_property_property_],
                                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                                else=component_property_property_,
                                                field="field",
                                                operand="operand",
                                                operand_type="operandType",
                                                operator="operator",
                                                property="property",
                                                then=component_property_property_
                                            ),
                                            configured=False,
                                            default_value="defaultValue",
                                            event="event",
                                            imported_value="importedValue",
                                            model="model",
                                            property="property",
                                            type="type",
                                            user_attribute="userAttribute",
                                            value="value"
                                        )
                                    ),
                                    target=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        bindings={
                                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                element="element",
                                                property="property"
                                            )
                                        },
                                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        component_name="componentName",
                                        concat=[component_property_property_],
                                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                            else=component_property_property_,
                                            field="field",
                                            operand="operand",
                                            operand_type="operandType",
                                            operator="operator",
                                            property="property",
                                            then=component_property_property_
                                        ),
                                        configured=False,
                                        default_value="defaultValue",
                                        event="event",
                                        imported_value="importedValue",
                                        model="model",
                                        property="property",
                                        type="type",
                                        user_attribute="userAttribute",
                                        value="value"
                                    ),
                                    type=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        bindings={
                                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                element="element",
                                                property="property"
                                            )
                                        },
                                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        component_name="componentName",
                                        concat=[component_property_property_],
                                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                            else=component_property_property_,
                                            field="field",
                                            operand="operand",
                                            operand_type="operandType",
                                            operator="operator",
                                            property="property",
                                            then=component_property_property_
                                        ),
                                        configured=False,
                                        default_value="defaultValue",
                                        event="event",
                                        imported_value="importedValue",
                                        model="model",
                                        property="property",
                                        type="type",
                                        user_attribute="userAttribute",
                                        value="value"
                                    ),
                                    url=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        bindings={
                                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                element="element",
                                                property="property"
                                            )
                                        },
                                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        component_name="componentName",
                                        concat=[component_property_property_],
                                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                            else=component_property_property_,
                                            field="field",
                                            operand="operand",
                                            operand_type="operandType",
                                            operator="operator",
                                            property="property",
                                            then=component_property_property_
                                        ),
                                        configured=False,
                                        default_value="defaultValue",
                                        event="event",
                                        imported_value="importedValue",
                                        model="model",
                                        property="property",
                                        type="type",
                                        user_attribute="userAttribute",
                                        value="value"
                                    )
                                )
                            )
                        }
                    )],
                    events={
                        "events_key": amplifyuibuilder.CfnComponent.ComponentEventProperty(
                            action="action",
                            parameters=amplifyuibuilder.CfnComponent.ActionParametersProperty(
                                anchor=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                ),
                                fields={
                                    "fields_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        bindings={
                                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                element="element",
                                                property="property"
                                            )
                                        },
                                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        component_name="componentName",
                                        concat=[component_property_property_],
                                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                            else=component_property_property_,
                                            field="field",
                                            operand="operand",
                                            operand_type="operandType",
                                            operator="operator",
                                            property="property",
                                            then=component_property_property_
                                        ),
                                        configured=False,
                                        default_value="defaultValue",
                                        event="event",
                                        imported_value="importedValue",
                                        model="model",
                                        property="property",
                                        type="type",
                                        user_attribute="userAttribute",
                                        value="value"
                                    )
                                },
                                global=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                ),
                                id=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                ),
                                model="model",
                                state=amplifyuibuilder.CfnComponent.MutationActionSetStateParameterProperty(
                                    component_name="componentName",
                                    property="property",
                                    set=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        bindings={
                                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                element="element",
                                                property="property"
                                            )
                                        },
                                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
                
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        component_name="componentName",
                                        concat=[component_property_property_],
                                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                            else=component_property_property_,
                                            field="field",
                                            operand="operand",
                                            operand_type="operandType",
                                            operator="operator",
                                            property="property",
                                            then=component_property_property_
                                        ),
                                        configured=False,
                                        default_value="defaultValue",
                                        event="event",
                                        imported_value="importedValue",
                                        model="model",
                                        property="property",
                                        type="type",
                                        user_attribute="userAttribute",
                                        value="value"
                                    )
                                ),
                                target=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                ),
                                type=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                ),
                                url=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
                
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                )
                            )
                        )
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3d50eae10e05ec6519c8b5405904b780a7f01613f52ff55abfb41b0c9edc884)
                check_type(argname="argument component_type", value=component_type, expected_type=type_hints["component_type"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
                check_type(argname="argument children", value=children, expected_type=type_hints["children"])
                check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "component_type": component_type,
                "name": name,
                "properties": properties,
            }
            if children is not None:
                self._values["children"] = children
            if events is not None:
                self._values["events"] = events

        @builtins.property
        def component_type(self) -> builtins.str:
            '''The type of the child component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html#cfn-amplifyuibuilder-component-componentchild-componenttype
            '''
            result = self._values.get("component_type")
            assert result is not None, "Required property 'component_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the child component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html#cfn-amplifyuibuilder-component-componentchild-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def properties(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]]:
            '''Describes the properties of the child component.

            You can't specify ``tags`` as a valid property for ``properties`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html#cfn-amplifyuibuilder-component-componentchild-properties
            '''
            result = self._values.get("properties")
            assert result is not None, "Required property 'properties' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def children(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.ComponentChildProperty", _IResolvable_da3f097b]]]]:
            '''The list of ``ComponentChild`` instances for this component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html#cfn-amplifyuibuilder-component-componentchild-children
            '''
            result = self._values.get("children")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.ComponentChildProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentEventProperty", _IResolvable_da3f097b]]]]:
            '''Describes the events that can be raised on the child component.

            Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html#cfn-amplifyuibuilder-component-componentchild-events
            '''
            result = self._values.get("events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.ComponentEventProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentChildProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "else_": "else",
            "field": "field",
            "operand": "operand",
            "operand_type": "operandType",
            "operator": "operator",
            "property": "property",
            "then": "then",
        },
    )
    class ComponentConditionPropertyProperty:
        def __init__(
            self,
            *,
            else_: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            field: typing.Optional[builtins.str] = None,
            operand: typing.Optional[builtins.str] = None,
            operand_type: typing.Optional[builtins.str] = None,
            operator: typing.Optional[builtins.str] = None,
            property: typing.Optional[builtins.str] = None,
            then: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``ComponentConditionProperty`` property specifies a conditional expression for setting a component property.

            Use ``ComponentConditionProperty`` to set a property to different values conditionally, based on the value of another property.

            :param else_: The value to assign to the property if the condition is not met.
            :param field: The name of a field. Specify this when the property is a data model.
            :param operand: The value of the property to evaluate.
            :param operand_type: The type of the property to evaluate.
            :param operator: The operator to use to perform the evaluation, such as ``eq`` to represent equals.
            :param property: The name of the conditional property.
            :param then: The value to assign to the property if the condition is met.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # component_property_property_: amplifyuibuilder.CfnComponent.ComponentPropertyProperty
                
                component_condition_property_property = amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                    else=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    ),
                    field="field",
                    operand="operand",
                    operand_type="operandType",
                    operator="operator",
                    property="property",
                    then=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9a087a026a105fe370e8b30547f8deb28449cbbc0ea16d6168c3ffe40b9fc3f7)
                check_type(argname="argument else_", value=else_, expected_type=type_hints["else_"])
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
                check_type(argname="argument operand", value=operand, expected_type=type_hints["operand"])
                check_type(argname="argument operand_type", value=operand_type, expected_type=type_hints["operand_type"])
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
                check_type(argname="argument property", value=property, expected_type=type_hints["property"])
                check_type(argname="argument then", value=then, expected_type=type_hints["then"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if else_ is not None:
                self._values["else_"] = else_
            if field is not None:
                self._values["field"] = field
            if operand is not None:
                self._values["operand"] = operand
            if operand_type is not None:
                self._values["operand_type"] = operand_type
            if operator is not None:
                self._values["operator"] = operator
            if property is not None:
                self._values["property"] = property
            if then is not None:
                self._values["then"] = then

        @builtins.property
        def else_(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]:
            '''The value to assign to the property if the condition is not met.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-else
            '''
            result = self._values.get("else_")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def field(self) -> typing.Optional[builtins.str]:
            '''The name of a field.

            Specify this when the property is a data model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-field
            '''
            result = self._values.get("field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operand(self) -> typing.Optional[builtins.str]:
            '''The value of the property to evaluate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-operand
            '''
            result = self._values.get("operand")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operand_type(self) -> typing.Optional[builtins.str]:
            '''The type of the property to evaluate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-operandtype
            '''
            result = self._values.get("operand_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operator(self) -> typing.Optional[builtins.str]:
            '''The operator to use to perform the evaluation, such as ``eq`` to represent equals.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-operator
            '''
            result = self._values.get("operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property(self) -> typing.Optional[builtins.str]:
            '''The name of the conditional property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-property
            '''
            result = self._values.get("property")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def then(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]:
            '''The value to assign to the property if the condition is met.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-then
            '''
            result = self._values.get("then")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConditionPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.ComponentDataConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "model": "model",
            "identifiers": "identifiers",
            "predicate": "predicate",
            "sort": "sort",
        },
    )
    class ComponentDataConfigurationProperty:
        def __init__(
            self,
            *,
            model: builtins.str,
            identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
            predicate: typing.Optional[typing.Union[typing.Union["CfnComponent.PredicateProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            sort: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnComponent.SortPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The ``ComponentDataConfiguration`` property specifies the configuration for binding a component's properties to data.

            :param model: The name of the data model to use to bind data to a component.
            :param identifiers: A list of IDs to use to bind data to a component. Use this property to bind specifically chosen data, rather than data retrieved from a query.
            :param predicate: Represents the conditional logic to use when binding data to a component. Use this property to retrieve only a subset of the data in a collection.
            :param sort: Describes how to sort the component's properties.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # predicate_property_: amplifyuibuilder.CfnComponent.PredicateProperty
                
                component_data_configuration_property = amplifyuibuilder.CfnComponent.ComponentDataConfigurationProperty(
                    model="model",
                
                    # the properties below are optional
                    identifiers=["identifiers"],
                    predicate=amplifyuibuilder.CfnComponent.PredicateProperty(
                        and=[predicate_property_],
                        field="field",
                        operand="operand",
                        operator="operator",
                        or=[predicate_property_]
                    ),
                    sort=[amplifyuibuilder.CfnComponent.SortPropertyProperty(
                        direction="direction",
                        field="field"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__64e141d7e4f47c6e1581f7d74ffea218f473c3420b88087f34835976ebac771f)
                check_type(argname="argument model", value=model, expected_type=type_hints["model"])
                check_type(argname="argument identifiers", value=identifiers, expected_type=type_hints["identifiers"])
                check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
                check_type(argname="argument sort", value=sort, expected_type=type_hints["sort"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "model": model,
            }
            if identifiers is not None:
                self._values["identifiers"] = identifiers
            if predicate is not None:
                self._values["predicate"] = predicate
            if sort is not None:
                self._values["sort"] = sort

        @builtins.property
        def model(self) -> builtins.str:
            '''The name of the data model to use to bind data to a component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html#cfn-amplifyuibuilder-component-componentdataconfiguration-model
            '''
            result = self._values.get("model")
            assert result is not None, "Required property 'model' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def identifiers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of IDs to use to bind data to a component.

            Use this property to bind specifically chosen data, rather than data retrieved from a query.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html#cfn-amplifyuibuilder-component-componentdataconfiguration-identifiers
            '''
            result = self._values.get("identifiers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def predicate(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.PredicateProperty", _IResolvable_da3f097b]]:
            '''Represents the conditional logic to use when binding data to a component.

            Use this property to retrieve only a subset of the data in a collection.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html#cfn-amplifyuibuilder-component-componentdataconfiguration-predicate
            '''
            result = self._values.get("predicate")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.PredicateProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def sort(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.SortPropertyProperty", _IResolvable_da3f097b]]]]:
            '''Describes how to sort the component's properties.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html#cfn-amplifyuibuilder-component-componentdataconfiguration-sort
            '''
            result = self._values.get("sort")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.SortPropertyProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentDataConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.ComponentEventProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action", "parameters": "parameters"},
    )
    class ComponentEventProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            parameters: typing.Optional[typing.Union[typing.Union["CfnComponent.ActionParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``ComponentEvent`` property specifies the configuration of an event.

            You can bind an event and a corresponding action to a ``Component`` or a ``ComponentChild`` . A button click is an example of an event.

            :param action: The action to perform when a specific event is raised.
            :param parameters: Describes information about the action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # component_property_property_: amplifyuibuilder.CfnComponent.ComponentPropertyProperty
                
                component_event_property = amplifyuibuilder.CfnComponent.ComponentEventProperty(
                    action="action",
                    parameters=amplifyuibuilder.CfnComponent.ActionParametersProperty(
                        anchor=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        fields={
                            "fields_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
                
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
                
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            )
                        },
                        global=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        id=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        model="model",
                        state=amplifyuibuilder.CfnComponent.MutationActionSetStateParameterProperty(
                            component_name="componentName",
                            property="property",
                            set=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
                
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
                
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            )
                        ),
                        target=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        type=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        url=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a2199271a6b5de84d37a061bced7624cc98fc5b38d9799e48008b25cc4beb30)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''The action to perform when a specific event is raised.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevent.html#cfn-amplifyuibuilder-component-componentevent-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ActionParametersProperty", _IResolvable_da3f097b]]:
            '''Describes information about the action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevent.html#cfn-amplifyuibuilder-component-componentevent-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ActionParametersProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"property": "property", "field": "field"},
    )
    class ComponentPropertyBindingPropertiesProperty:
        def __init__(
            self,
            *,
            property: builtins.str,
            field: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``ComponentPropertyBindingProperties`` property specifies a component property to associate with a binding property.

            This enables exposed properties on the top level component to propagate data to the component's property values.

            :param property: The component property to bind to the data field.
            :param field: The data field to bind the property to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentpropertybindingproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                component_property_binding_properties_property = amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                    property="property",
                
                    # the properties below are optional
                    field="field"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6609f397f447132bed1b4dae768619a73958cd6fb765edd0f7a2623013c57096)
                check_type(argname="argument property", value=property, expected_type=type_hints["property"])
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "property": property,
            }
            if field is not None:
                self._values["field"] = field

        @builtins.property
        def property(self) -> builtins.str:
            '''The component property to bind to the data field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentpropertybindingproperties.html#cfn-amplifyuibuilder-component-componentpropertybindingproperties-property
            '''
            result = self._values.get("property")
            assert result is not None, "Required property 'property' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def field(self) -> typing.Optional[builtins.str]:
            '''The data field to bind the property to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentpropertybindingproperties.html#cfn-amplifyuibuilder-component-componentpropertybindingproperties-field
            '''
            result = self._values.get("field")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentPropertyBindingPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.ComponentPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "binding_properties": "bindingProperties",
            "bindings": "bindings",
            "collection_binding_properties": "collectionBindingProperties",
            "component_name": "componentName",
            "concat": "concat",
            "condition": "condition",
            "configured": "configured",
            "default_value": "defaultValue",
            "event": "event",
            "imported_value": "importedValue",
            "model": "model",
            "property": "property",
            "type": "type",
            "user_attribute": "userAttribute",
            "value": "value",
        },
    )
    class ComponentPropertyProperty:
        def __init__(
            self,
            *,
            binding_properties: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentPropertyBindingPropertiesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            bindings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnComponent.FormBindingElementProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            collection_binding_properties: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentPropertyBindingPropertiesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            component_name: typing.Optional[builtins.str] = None,
            concat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            condition: typing.Optional[typing.Union[typing.Union["CfnComponent.ComponentConditionPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            configured: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            default_value: typing.Optional[builtins.str] = None,
            event: typing.Optional[builtins.str] = None,
            imported_value: typing.Optional[builtins.str] = None,
            model: typing.Optional[builtins.str] = None,
            property: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            user_attribute: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``ComponentProperty`` property specifies the configuration for all of a component's properties.

            Use ``ComponentProperty`` to specify the values to render or bind by default.

            :param binding_properties: The information to bind the component property to data at runtime.
            :param bindings: The information to bind the component property to form data.
            :param collection_binding_properties: The information to bind the component property to data at runtime. Use this for collection components.
            :param component_name: The name of the component that is affected by an event.
            :param concat: A list of component properties to concatenate to create the value to assign to this component property.
            :param condition: The conditional expression to use to assign a value to the component property.
            :param configured: Specifies whether the user configured the property in Amplify Studio after importing it.
            :param default_value: The default value to assign to the component property.
            :param event: An event that occurs in your app. Use this for workflow data binding.
            :param imported_value: The default value assigned to the property when the component is imported into an app.
            :param model: The data model to use to assign a value to the component property.
            :param property: The name of the component's property that is affected by an event.
            :param type: The component type.
            :param user_attribute: An authenticated user attribute to use to assign a value to the component property.
            :param value: The value to assign to the component property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # component_condition_property_property_: amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty
                # component_property_property_: amplifyuibuilder.CfnComponent.ComponentPropertyProperty
                
                component_property_property = amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                        property="property",
                
                        # the properties below are optional
                        field="field"
                    ),
                    bindings={
                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                            element="element",
                            property="property"
                        )
                    },
                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                        property="property",
                
                        # the properties below are optional
                        field="field"
                    ),
                    component_name="componentName",
                    concat=[amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    )],
                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                        else=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=component_condition_property_property_,
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        ),
                        field="field",
                        operand="operand",
                        operand_type="operandType",
                        operator="operator",
                        property="property",
                        then=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
                
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=component_condition_property_property_,
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        )
                    ),
                    configured=False,
                    default_value="defaultValue",
                    event="event",
                    imported_value="importedValue",
                    model="model",
                    property="property",
                    type="type",
                    user_attribute="userAttribute",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9cf7d407c19a13b1e358d52a06851a4288f7e5e365289ff8c22d9b2d67d8d179)
                check_type(argname="argument binding_properties", value=binding_properties, expected_type=type_hints["binding_properties"])
                check_type(argname="argument bindings", value=bindings, expected_type=type_hints["bindings"])
                check_type(argname="argument collection_binding_properties", value=collection_binding_properties, expected_type=type_hints["collection_binding_properties"])
                check_type(argname="argument component_name", value=component_name, expected_type=type_hints["component_name"])
                check_type(argname="argument concat", value=concat, expected_type=type_hints["concat"])
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
                check_type(argname="argument configured", value=configured, expected_type=type_hints["configured"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument event", value=event, expected_type=type_hints["event"])
                check_type(argname="argument imported_value", value=imported_value, expected_type=type_hints["imported_value"])
                check_type(argname="argument model", value=model, expected_type=type_hints["model"])
                check_type(argname="argument property", value=property, expected_type=type_hints["property"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument user_attribute", value=user_attribute, expected_type=type_hints["user_attribute"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if binding_properties is not None:
                self._values["binding_properties"] = binding_properties
            if bindings is not None:
                self._values["bindings"] = bindings
            if collection_binding_properties is not None:
                self._values["collection_binding_properties"] = collection_binding_properties
            if component_name is not None:
                self._values["component_name"] = component_name
            if concat is not None:
                self._values["concat"] = concat
            if condition is not None:
                self._values["condition"] = condition
            if configured is not None:
                self._values["configured"] = configured
            if default_value is not None:
                self._values["default_value"] = default_value
            if event is not None:
                self._values["event"] = event
            if imported_value is not None:
                self._values["imported_value"] = imported_value
            if model is not None:
                self._values["model"] = model
            if property is not None:
                self._values["property"] = property
            if type is not None:
                self._values["type"] = type
            if user_attribute is not None:
                self._values["user_attribute"] = user_attribute
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def binding_properties(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentPropertyBindingPropertiesProperty", _IResolvable_da3f097b]]:
            '''The information to bind the component property to data at runtime.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-bindingproperties
            '''
            result = self._values.get("binding_properties")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentPropertyBindingPropertiesProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def bindings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.FormBindingElementProperty", _IResolvable_da3f097b]]]]:
            '''The information to bind the component property to form data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-bindings
            '''
            result = self._values.get("bindings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnComponent.FormBindingElementProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def collection_binding_properties(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentPropertyBindingPropertiesProperty", _IResolvable_da3f097b]]:
            '''The information to bind the component property to data at runtime.

            Use this for collection components.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-collectionbindingproperties
            '''
            result = self._values.get("collection_binding_properties")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentPropertyBindingPropertiesProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def component_name(self) -> typing.Optional[builtins.str]:
            '''The name of the component that is affected by an event.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-componentname
            '''
            result = self._values.get("component_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def concat(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]]]:
            '''A list of component properties to concatenate to create the value to assign to this component property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-concat
            '''
            result = self._values.get("concat")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def condition(
            self,
        ) -> typing.Optional[typing.Union["CfnComponent.ComponentConditionPropertyProperty", _IResolvable_da3f097b]]:
            '''The conditional expression to use to assign a value to the component property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-condition
            '''
            result = self._values.get("condition")
            return typing.cast(typing.Optional[typing.Union["CfnComponent.ComponentConditionPropertyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def configured(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the user configured the property in Amplify Studio after importing it.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-configured
            '''
            result = self._values.get("configured")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''The default value to assign to the component property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event(self) -> typing.Optional[builtins.str]:
            '''An event that occurs in your app.

            Use this for workflow data binding.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-event
            '''
            result = self._values.get("event")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def imported_value(self) -> typing.Optional[builtins.str]:
            '''The default value assigned to the property when the component is imported into an app.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-importedvalue
            '''
            result = self._values.get("imported_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def model(self) -> typing.Optional[builtins.str]:
            '''The data model to use to assign a value to the component property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-model
            '''
            result = self._values.get("model")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property(self) -> typing.Optional[builtins.str]:
            '''The name of the component's property that is affected by an event.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-property
            '''
            result = self._values.get("property")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The component type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_attribute(self) -> typing.Optional[builtins.str]:
            '''An authenticated user attribute to use to assign a value to the component property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-userattribute
            '''
            result = self._values.get("user_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value to assign to the component property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.ComponentVariantProperty",
        jsii_struct_bases=[],
        name_mapping={"overrides": "overrides", "variant_values": "variantValues"},
    )
    class ComponentVariantProperty:
        def __init__(
            self,
            *,
            overrides: typing.Any = None,
            variant_values: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''The ``ComponentVariant`` property specifies the style configuration of a unique variation of a main component.

            :param overrides: The properties of the component variant that can be overriden when customizing an instance of the component. You can't specify ``tags`` as a valid property for ``overrides`` .
            :param variant_values: The combination of variants that comprise this variant.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentvariant.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # overrides: Any
                
                component_variant_property = amplifyuibuilder.CfnComponent.ComponentVariantProperty(
                    overrides=overrides,
                    variant_values={
                        "variant_values_key": "variantValues"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__295e4045520d86ca93a4865404c10aafdb49dd91806c9cae31545fdd54e9bee9)
                check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
                check_type(argname="argument variant_values", value=variant_values, expected_type=type_hints["variant_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if overrides is not None:
                self._values["overrides"] = overrides
            if variant_values is not None:
                self._values["variant_values"] = variant_values

        @builtins.property
        def overrides(self) -> typing.Any:
            '''The properties of the component variant that can be overriden when customizing an instance of the component.

            You can't specify ``tags`` as a valid property for ``overrides`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentvariant.html#cfn-amplifyuibuilder-component-componentvariant-overrides
            '''
            result = self._values.get("overrides")
            return typing.cast(typing.Any, result)

        @builtins.property
        def variant_values(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The combination of variants that comprise this variant.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentvariant.html#cfn-amplifyuibuilder-component-componentvariant-variantvalues
            '''
            result = self._values.get("variant_values")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentVariantProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.FormBindingElementProperty",
        jsii_struct_bases=[],
        name_mapping={"element": "element", "property": "property"},
    )
    class FormBindingElementProperty:
        def __init__(self, *, element: builtins.str, property: builtins.str) -> None:
            '''
            :param element: ``CfnComponent.FormBindingElementProperty.Element``.
            :param property: ``CfnComponent.FormBindingElementProperty.Property``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-formbindingelement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                form_binding_element_property = amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                    element="element",
                    property="property"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__083b2206ecf6efde86ba8aefa3608c36f293532c3f9ff7e1ec5724b9f2540d0a)
                check_type(argname="argument element", value=element, expected_type=type_hints["element"])
                check_type(argname="argument property", value=property, expected_type=type_hints["property"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "element": element,
                "property": property,
            }

        @builtins.property
        def element(self) -> builtins.str:
            '''``CfnComponent.FormBindingElementProperty.Element``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-formbindingelement.html#cfn-amplifyuibuilder-component-formbindingelement-element
            '''
            result = self._values.get("element")
            assert result is not None, "Required property 'element' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def property(self) -> builtins.str:
            '''``CfnComponent.FormBindingElementProperty.Property``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-formbindingelement.html#cfn-amplifyuibuilder-component-formbindingelement-property
            '''
            result = self._values.get("property")
            assert result is not None, "Required property 'property' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormBindingElementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.MutationActionSetStateParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_name": "componentName",
            "property": "property",
            "set": "set",
        },
    )
    class MutationActionSetStateParameterProperty:
        def __init__(
            self,
            *,
            component_name: builtins.str,
            property: builtins.str,
            set: typing.Union[typing.Union["CfnComponent.ComponentPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        ) -> None:
            '''The ``MutationActionSetStateParameter`` property specifies the state configuration when an action modifies a property of another element within the same component.

            :param component_name: The name of the component that is being modified.
            :param property: The name of the component property to apply the state configuration to.
            :param set: The state configuration to assign to the property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # component_property_property_: amplifyuibuilder.CfnComponent.ComponentPropertyProperty
                
                mutation_action_set_state_parameter_property = amplifyuibuilder.CfnComponent.MutationActionSetStateParameterProperty(
                    component_name="componentName",
                    property="property",
                    set=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
                
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a2c7bf8adc174a1333d4f6712bb6a171a89b27809627e9e7265e3d111f78189a)
                check_type(argname="argument component_name", value=component_name, expected_type=type_hints["component_name"])
                check_type(argname="argument property", value=property, expected_type=type_hints["property"])
                check_type(argname="argument set", value=set, expected_type=type_hints["set"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "component_name": component_name,
                "property": property,
                "set": set,
            }

        @builtins.property
        def component_name(self) -> builtins.str:
            '''The name of the component that is being modified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-componentname
            '''
            result = self._values.get("component_name")
            assert result is not None, "Required property 'component_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def property(self) -> builtins.str:
            '''The name of the component property to apply the state configuration to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-property
            '''
            result = self._values.get("property")
            assert result is not None, "Required property 'property' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def set(
            self,
        ) -> typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b]:
            '''The state configuration to assign to the property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-set
            '''
            result = self._values.get("set")
            assert result is not None, "Required property 'set' is missing"
            return typing.cast(typing.Union["CfnComponent.ComponentPropertyProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MutationActionSetStateParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.PredicateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_": "and",
            "field": "field",
            "operand": "operand",
            "operator": "operator",
            "or_": "or",
        },
    )
    class PredicateProperty:
        def __init__(
            self,
            *,
            and_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnComponent.PredicateProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            field: typing.Optional[builtins.str] = None,
            operand: typing.Optional[builtins.str] = None,
            operator: typing.Optional[builtins.str] = None,
            or_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnComponent.PredicateProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The ``Predicate`` property specifies information for generating Amplify DataStore queries.

            Use ``Predicate`` to retrieve a subset of the data in a collection.

            :param and_: A list of predicates to combine logically.
            :param field: The field to query.
            :param operand: The value to use when performing the evaluation.
            :param operator: The operator to use to perform the evaluation.
            :param or_: A list of predicates to combine logically.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # predicate_property_: amplifyuibuilder.CfnComponent.PredicateProperty
                
                predicate_property = amplifyuibuilder.CfnComponent.PredicateProperty(
                    and=[amplifyuibuilder.CfnComponent.PredicateProperty(
                        and=[predicate_property_],
                        field="field",
                        operand="operand",
                        operator="operator",
                        or=[predicate_property_]
                    )],
                    field="field",
                    operand="operand",
                    operator="operator",
                    or=[amplifyuibuilder.CfnComponent.PredicateProperty(
                        and=[predicate_property_],
                        field="field",
                        operand="operand",
                        operator="operator",
                        or=[predicate_property_]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__37ce81ce3ae3ad1d19dadf5542dca7cb3465cd10747b81f17e473f6a27342336)
                check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
                check_type(argname="argument operand", value=operand, expected_type=type_hints["operand"])
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
                check_type(argname="argument or_", value=or_, expected_type=type_hints["or_"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if and_ is not None:
                self._values["and_"] = and_
            if field is not None:
                self._values["field"] = field
            if operand is not None:
                self._values["operand"] = operand
            if operator is not None:
                self._values["operator"] = operator
            if or_ is not None:
                self._values["or_"] = or_

        @builtins.property
        def and_(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.PredicateProperty", _IResolvable_da3f097b]]]]:
            '''A list of predicates to combine logically.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html#cfn-amplifyuibuilder-component-predicate-and
            '''
            result = self._values.get("and_")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.PredicateProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def field(self) -> typing.Optional[builtins.str]:
            '''The field to query.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html#cfn-amplifyuibuilder-component-predicate-field
            '''
            result = self._values.get("field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operand(self) -> typing.Optional[builtins.str]:
            '''The value to use when performing the evaluation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html#cfn-amplifyuibuilder-component-predicate-operand
            '''
            result = self._values.get("operand")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operator(self) -> typing.Optional[builtins.str]:
            '''The operator to use to perform the evaluation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html#cfn-amplifyuibuilder-component-predicate-operator
            '''
            result = self._values.get("operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def or_(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.PredicateProperty", _IResolvable_da3f097b]]]]:
            '''A list of predicates to combine logically.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html#cfn-amplifyuibuilder-component-predicate-or
            '''
            result = self._values.get("or_")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnComponent.PredicateProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredicateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponent.SortPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"direction": "direction", "field": "field"},
    )
    class SortPropertyProperty:
        def __init__(self, *, direction: builtins.str, field: builtins.str) -> None:
            '''The ``SortProperty`` property specifies how to sort the data that you bind to a component.

            :param direction: The direction of the sort, either ascending or descending.
            :param field: The field to perform the sort on.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-sortproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                sort_property_property = amplifyuibuilder.CfnComponent.SortPropertyProperty(
                    direction="direction",
                    field="field"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e28aa12f1ac083d97c2507afcccfed6130be39825a273208c629b58a9826c9d)
                check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "direction": direction,
                "field": field,
            }

        @builtins.property
        def direction(self) -> builtins.str:
            '''The direction of the sort, either ascending or descending.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-sortproperty.html#cfn-amplifyuibuilder-component-sortproperty-direction
            '''
            result = self._values.get("direction")
            assert result is not None, "Required property 'direction' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def field(self) -> builtins.str:
            '''The field to perform the sort on.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-sortproperty.html#cfn-amplifyuibuilder-component-sortproperty-field
            '''
            result = self._values.get("field")
            assert result is not None, "Required property 'field' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SortPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnComponentProps",
    jsii_struct_bases=[],
    name_mapping={
        "binding_properties": "bindingProperties",
        "component_type": "componentType",
        "name": "name",
        "overrides": "overrides",
        "properties": "properties",
        "variants": "variants",
        "children": "children",
        "collection_properties": "collectionProperties",
        "events": "events",
        "schema_version": "schemaVersion",
        "source_id": "sourceId",
        "tags": "tags",
    },
)
class CfnComponentProps:
    def __init__(
        self,
        *,
        binding_properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentBindingPropertiesValueProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        component_type: builtins.str,
        name: builtins.str,
        overrides: typing.Any,
        properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        variants: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.ComponentVariantProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        children: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.ComponentChildProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        collection_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentDataConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentEventProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        schema_version: typing.Optional[builtins.str] = None,
        source_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnComponent``.

        :param binding_properties: The information to connect a component's properties to data at runtime. You can't specify ``tags`` as a valid property for ``bindingProperties`` .
        :param component_type: The type of the component. This can be an Amplify custom UI component or another custom component.
        :param name: The name of the component.
        :param overrides: Describes the component's properties that can be overriden in a customized instance of the component. You can't specify ``tags`` as a valid property for ``overrides`` .
        :param properties: Describes the component's properties. You can't specify ``tags`` as a valid property for ``properties`` .
        :param variants: A list of the component's variants. A variant is a unique style configuration of a main component.
        :param children: A list of the component's ``ComponentChild`` instances.
        :param collection_properties: The data binding configuration for the component's properties. Use this for a collection component. You can't specify ``tags`` as a valid property for ``collectionProperties`` .
        :param events: Describes the events that can be raised on the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
        :param schema_version: The schema version of the component when it was imported.
        :param source_id: The unique ID of the component in its original source system, such as Figma.
        :param tags: One or more key-value pairs to use when tagging the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
            
            # component_child_property_: amplifyuibuilder.CfnComponent.ComponentChildProperty
            # component_property_property_: amplifyuibuilder.CfnComponent.ComponentPropertyProperty
            # overrides: Any
            # predicate_property_: amplifyuibuilder.CfnComponent.PredicateProperty
            
            cfn_component_props = amplifyuibuilder.CfnComponentProps(
                binding_properties={
                    "binding_properties_key": amplifyuibuilder.CfnComponent.ComponentBindingPropertiesValueProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentBindingPropertiesValuePropertiesProperty(
                            bucket="bucket",
                            default_value="defaultValue",
                            field="field",
                            key="key",
                            model="model",
                            predicates=[amplifyuibuilder.CfnComponent.PredicateProperty(
                                and=[predicate_property_],
                                field="field",
                                operand="operand",
                                operator="operator",
                                or=[predicate_property_]
                            )],
                            user_attribute="userAttribute"
                        ),
                        default_value="defaultValue",
                        type="type"
                    )
                },
                component_type="componentType",
                name="name",
                overrides=overrides,
                properties={
                    "properties_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
            
                            # the properties below are optional
                            field="field"
                        ),
                        bindings={
                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                element="element",
                                property="property"
                            )
                        },
                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                            property="property",
            
                            # the properties below are optional
                            field="field"
                        ),
                        component_name="componentName",
                        concat=[component_property_property_],
                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                            else=component_property_property_,
                            field="field",
                            operand="operand",
                            operand_type="operandType",
                            operator="operator",
                            property="property",
                            then=component_property_property_
                        ),
                        configured=False,
                        default_value="defaultValue",
                        event="event",
                        imported_value="importedValue",
                        model="model",
                        property="property",
                        type="type",
                        user_attribute="userAttribute",
                        value="value"
                    )
                },
                variants=[amplifyuibuilder.CfnComponent.ComponentVariantProperty(
                    overrides=overrides,
                    variant_values={
                        "variant_values_key": "variantValues"
                    }
                )],
            
                # the properties below are optional
                children=[amplifyuibuilder.CfnComponent.ComponentChildProperty(
                    component_type="componentType",
                    name="name",
                    properties={
                        "properties_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                            binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
            
                                # the properties below are optional
                                field="field"
                            ),
                            bindings={
                                "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                    element="element",
                                    property="property"
                                )
                            },
                            collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                property="property",
            
                                # the properties below are optional
                                field="field"
                            ),
                            component_name="componentName",
                            concat=[component_property_property_],
                            condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                else=component_property_property_,
                                field="field",
                                operand="operand",
                                operand_type="operandType",
                                operator="operator",
                                property="property",
                                then=component_property_property_
                            ),
                            configured=False,
                            default_value="defaultValue",
                            event="event",
                            imported_value="importedValue",
                            model="model",
                            property="property",
                            type="type",
                            user_attribute="userAttribute",
                            value="value"
                        )
                    },
            
                    # the properties below are optional
                    children=[component_child_property_],
                    events={
                        "events_key": amplifyuibuilder.CfnComponent.ComponentEventProperty(
                            action="action",
                            parameters=amplifyuibuilder.CfnComponent.ActionParametersProperty(
                                anchor=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                ),
                                fields={
                                    "fields_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
            
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        bindings={
                                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                element="element",
                                                property="property"
                                            )
                                        },
                                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
            
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        component_name="componentName",
                                        concat=[component_property_property_],
                                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                            else=component_property_property_,
                                            field="field",
                                            operand="operand",
                                            operand_type="operandType",
                                            operator="operator",
                                            property="property",
                                            then=component_property_property_
                                        ),
                                        configured=False,
                                        default_value="defaultValue",
                                        event="event",
                                        imported_value="importedValue",
                                        model="model",
                                        property="property",
                                        type="type",
                                        user_attribute="userAttribute",
                                        value="value"
                                    )
                                },
                                global=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                ),
                                id=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                ),
                                model="model",
                                state=amplifyuibuilder.CfnComponent.MutationActionSetStateParameterProperty(
                                    component_name="componentName",
                                    property="property",
                                    set=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                        binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
            
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        bindings={
                                            "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                                element="element",
                                                property="property"
                                            )
                                        },
                                        collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                            property="property",
            
                                            # the properties below are optional
                                            field="field"
                                        ),
                                        component_name="componentName",
                                        concat=[component_property_property_],
                                        condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                            else=component_property_property_,
                                            field="field",
                                            operand="operand",
                                            operand_type="operandType",
                                            operator="operator",
                                            property="property",
                                            then=component_property_property_
                                        ),
                                        configured=False,
                                        default_value="defaultValue",
                                        event="event",
                                        imported_value="importedValue",
                                        model="model",
                                        property="property",
                                        type="type",
                                        user_attribute="userAttribute",
                                        value="value"
                                    )
                                ),
                                target=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                ),
                                type=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                ),
                                url=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                )
                            )
                        )
                    }
                )],
                collection_properties={
                    "collection_properties_key": amplifyuibuilder.CfnComponent.ComponentDataConfigurationProperty(
                        model="model",
            
                        # the properties below are optional
                        identifiers=["identifiers"],
                        predicate=amplifyuibuilder.CfnComponent.PredicateProperty(
                            and=[predicate_property_],
                            field="field",
                            operand="operand",
                            operator="operator",
                            or=[predicate_property_]
                        ),
                        sort=[amplifyuibuilder.CfnComponent.SortPropertyProperty(
                            direction="direction",
                            field="field"
                        )]
                    )
                },
                events={
                    "events_key": amplifyuibuilder.CfnComponent.ComponentEventProperty(
                        action="action",
                        parameters=amplifyuibuilder.CfnComponent.ActionParametersProperty(
                            anchor=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            ),
                            fields={
                                "fields_key": amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                )
                            },
                            global=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            ),
                            id=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            ),
                            model="model",
                            state=amplifyuibuilder.CfnComponent.MutationActionSetStateParameterProperty(
                                component_name="componentName",
                                property="property",
                                set=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                    binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    bindings={
                                        "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                            element="element",
                                            property="property"
                                        )
                                    },
                                    collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                        property="property",
            
                                        # the properties below are optional
                                        field="field"
                                    ),
                                    component_name="componentName",
                                    concat=[component_property_property_],
                                    condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                        else=component_property_property_,
                                        field="field",
                                        operand="operand",
                                        operand_type="operandType",
                                        operator="operator",
                                        property="property",
                                        then=component_property_property_
                                    ),
                                    configured=False,
                                    default_value="defaultValue",
                                    event="event",
                                    imported_value="importedValue",
                                    model="model",
                                    property="property",
                                    type="type",
                                    user_attribute="userAttribute",
                                    value="value"
                                )
                            ),
                            target=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            ),
                            type=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            ),
                            url=amplifyuibuilder.CfnComponent.ComponentPropertyProperty(
                                binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                bindings={
                                    "bindings_key": amplifyuibuilder.CfnComponent.FormBindingElementProperty(
                                        element="element",
                                        property="property"
                                    )
                                },
                                collection_binding_properties=amplifyuibuilder.CfnComponent.ComponentPropertyBindingPropertiesProperty(
                                    property="property",
            
                                    # the properties below are optional
                                    field="field"
                                ),
                                component_name="componentName",
                                concat=[component_property_property_],
                                condition=amplifyuibuilder.CfnComponent.ComponentConditionPropertyProperty(
                                    else=component_property_property_,
                                    field="field",
                                    operand="operand",
                                    operand_type="operandType",
                                    operator="operator",
                                    property="property",
                                    then=component_property_property_
                                ),
                                configured=False,
                                default_value="defaultValue",
                                event="event",
                                imported_value="importedValue",
                                model="model",
                                property="property",
                                type="type",
                                user_attribute="userAttribute",
                                value="value"
                            )
                        )
                    )
                },
                schema_version="schemaVersion",
                source_id="sourceId",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f53200a7ca068c25e3052be6f1490d18f9816b65f2cfec3a854a23ba3d5e5f45)
            check_type(argname="argument binding_properties", value=binding_properties, expected_type=type_hints["binding_properties"])
            check_type(argname="argument component_type", value=component_type, expected_type=type_hints["component_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument variants", value=variants, expected_type=type_hints["variants"])
            check_type(argname="argument children", value=children, expected_type=type_hints["children"])
            check_type(argname="argument collection_properties", value=collection_properties, expected_type=type_hints["collection_properties"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument schema_version", value=schema_version, expected_type=type_hints["schema_version"])
            check_type(argname="argument source_id", value=source_id, expected_type=type_hints["source_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "binding_properties": binding_properties,
            "component_type": component_type,
            "name": name,
            "overrides": overrides,
            "properties": properties,
            "variants": variants,
        }
        if children is not None:
            self._values["children"] = children
        if collection_properties is not None:
            self._values["collection_properties"] = collection_properties
        if events is not None:
            self._values["events"] = events
        if schema_version is not None:
            self._values["schema_version"] = schema_version
        if source_id is not None:
            self._values["source_id"] = source_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def binding_properties(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentBindingPropertiesValueProperty, _IResolvable_da3f097b]]]:
        '''The information to connect a component's properties to data at runtime.

        You can't specify ``tags`` as a valid property for ``bindingProperties`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-bindingproperties
        '''
        result = self._values.get("binding_properties")
        assert result is not None, "Required property 'binding_properties' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentBindingPropertiesValueProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def component_type(self) -> builtins.str:
        '''The type of the component.

        This can be an Amplify custom UI component or another custom component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-componenttype
        '''
        result = self._values.get("component_type")
        assert result is not None, "Required property 'component_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def overrides(self) -> typing.Any:
        '''Describes the component's properties that can be overriden in a customized instance of the component.

        You can't specify ``tags`` as a valid property for ``overrides`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-overrides
        '''
        result = self._values.get("overrides")
        assert result is not None, "Required property 'overrides' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def properties(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentPropertyProperty, _IResolvable_da3f097b]]]:
        '''Describes the component's properties.

        You can't specify ``tags`` as a valid property for ``properties`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-properties
        '''
        result = self._values.get("properties")
        assert result is not None, "Required property 'properties' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentPropertyProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def variants(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnComponent.ComponentVariantProperty, _IResolvable_da3f097b]]]:
        '''A list of the component's variants.

        A variant is a unique style configuration of a main component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-variants
        '''
        result = self._values.get("variants")
        assert result is not None, "Required property 'variants' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnComponent.ComponentVariantProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def children(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnComponent.ComponentChildProperty, _IResolvable_da3f097b]]]]:
        '''A list of the component's ``ComponentChild`` instances.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-children
        '''
        result = self._values.get("children")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnComponent.ComponentChildProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def collection_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentDataConfigurationProperty, _IResolvable_da3f097b]]]]:
        '''The data binding configuration for the component's properties.

        Use this for a collection component. You can't specify ``tags`` as a valid property for ``collectionProperties`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-collectionproperties
        '''
        result = self._values.get("collection_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentDataConfigurationProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def events(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentEventProperty, _IResolvable_da3f097b]]]]:
        '''Describes the events that can be raised on the component.

        Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-events
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentEventProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def schema_version(self) -> typing.Optional[builtins.str]:
        '''The schema version of the component when it was imported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-schemaversion
        '''
        result = self._values.get("schema_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_id(self) -> typing.Optional[builtins.str]:
        '''The unique ID of the component in its original source system, such as Figma.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-sourceid
        '''
        result = self._values.get("source_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''One or more key-value pairs to use when tagging the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComponentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnForm(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm",
):
    '''A CloudFormation ``AWS::AmplifyUIBuilder::Form``.

    :cloudformationResource: AWS::AmplifyUIBuilder::Form
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
        
        cfn_form = amplifyuibuilder.CfnForm(self, "MyCfnForm",
            data_type=amplifyuibuilder.CfnForm.FormDataTypeConfigProperty(
                data_source_type="dataSourceType",
                data_type_name="dataTypeName"
            ),
            fields={
                "fields_key": amplifyuibuilder.CfnForm.FieldConfigProperty(
                    excluded=False,
                    input_type=amplifyuibuilder.CfnForm.FieldInputConfigProperty(
                        type="type",
        
                        # the properties below are optional
                        default_checked=False,
                        default_country_code="defaultCountryCode",
                        default_value="defaultValue",
                        descriptive_text="descriptiveText",
                        max_value=123,
                        min_value=123,
                        name="name",
                        placeholder="placeholder",
                        read_only=False,
                        required=False,
                        step=123,
                        value="value",
                        value_mappings=amplifyuibuilder.CfnForm.ValueMappingsProperty(
                            values=[amplifyuibuilder.CfnForm.ValueMappingProperty(
                                value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                                    value="value"
                                ),
        
                                # the properties below are optional
                                display_value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                                    value="value"
                                )
                            )]
                        )
                    ),
                    label="label",
                    position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                        below="below",
                        fixed="fixed",
                        right_of="rightOf"
                    ),
                    validations=[amplifyuibuilder.CfnForm.FieldValidationConfigurationProperty(
                        type="type",
        
                        # the properties below are optional
                        num_values=[123],
                        str_values=["strValues"],
                        validation_message="validationMessage"
                    )]
                )
            },
            form_action_type="formActionType",
            name="name",
            schema_version="schemaVersion",
            sectional_elements={
                "sectional_elements_key": amplifyuibuilder.CfnForm.SectionalElementProperty(
                    type="type",
        
                    # the properties below are optional
                    level=123,
                    orientation="orientation",
                    position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                        below="below",
                        fixed="fixed",
                        right_of="rightOf"
                    ),
                    text="text"
                )
            },
            style=amplifyuibuilder.CfnForm.FormStyleProperty(
                horizontal_gap=amplifyuibuilder.CfnForm.FormStyleConfigProperty(
                    token_reference="tokenReference",
                    value="value"
                ),
                outer_padding=amplifyuibuilder.CfnForm.FormStyleConfigProperty(
                    token_reference="tokenReference",
                    value="value"
                ),
                vertical_gap=amplifyuibuilder.CfnForm.FormStyleConfigProperty(
                    token_reference="tokenReference",
                    value="value"
                )
            ),
        
            # the properties below are optional
            app_id="appId",
            cta=amplifyuibuilder.CfnForm.FormCTAProperty(
                cancel=amplifyuibuilder.CfnForm.FormButtonProperty(
                    children="children",
                    excluded=False,
                    position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                        below="below",
                        fixed="fixed",
                        right_of="rightOf"
                    )
                ),
                clear=amplifyuibuilder.CfnForm.FormButtonProperty(
                    children="children",
                    excluded=False,
                    position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                        below="below",
                        fixed="fixed",
                        right_of="rightOf"
                    )
                ),
                position="position",
                submit=amplifyuibuilder.CfnForm.FormButtonProperty(
                    children="children",
                    excluded=False,
                    position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                        below="below",
                        fixed="fixed",
                        right_of="rightOf"
                    )
                )
            ),
            environment_name="environmentName",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_type: typing.Union[typing.Union["CfnForm.FormDataTypeConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        fields: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnForm.FieldConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        form_action_type: builtins.str,
        name: builtins.str,
        schema_version: builtins.str,
        sectional_elements: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnForm.SectionalElementProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        style: typing.Union[typing.Union["CfnForm.FormStyleProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        app_id: typing.Optional[builtins.str] = None,
        cta: typing.Optional[typing.Union[typing.Union["CfnForm.FormCTAProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        environment_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::AmplifyUIBuilder::Form``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_type: ``AWS::AmplifyUIBuilder::Form.DataType``.
        :param fields: ``AWS::AmplifyUIBuilder::Form.Fields``.
        :param form_action_type: ``AWS::AmplifyUIBuilder::Form.FormActionType``.
        :param name: ``AWS::AmplifyUIBuilder::Form.Name``.
        :param schema_version: ``AWS::AmplifyUIBuilder::Form.SchemaVersion``.
        :param sectional_elements: ``AWS::AmplifyUIBuilder::Form.SectionalElements``.
        :param style: ``AWS::AmplifyUIBuilder::Form.Style``.
        :param app_id: ``AWS::AmplifyUIBuilder::Form.AppId``.
        :param cta: ``AWS::AmplifyUIBuilder::Form.Cta``.
        :param environment_name: ``AWS::AmplifyUIBuilder::Form.EnvironmentName``.
        :param tags: ``AWS::AmplifyUIBuilder::Form.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1e1e67668c27ec66bb2b6aa2fd792ed1f3347990281e8dd83ae2ac8e81aaac8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFormProps(
            data_type=data_type,
            fields=fields,
            form_action_type=form_action_type,
            name=name,
            schema_version=schema_version,
            sectional_elements=sectional_elements,
            style=style,
            app_id=app_id,
            cta=cta,
            environment_name=environment_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c21e8cabf9d014e4b7da846798df9ed12d78b23e1e4bc708e80a16526466e109)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8dedc67622f4e478423a2acbe47f789044cbf9bf399c9f14ba25932fda2994e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::AmplifyUIBuilder::Form.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(
        self,
    ) -> typing.Union["CfnForm.FormDataTypeConfigProperty", _IResolvable_da3f097b]:
        '''``AWS::AmplifyUIBuilder::Form.DataType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-datatype
        '''
        return typing.cast(typing.Union["CfnForm.FormDataTypeConfigProperty", _IResolvable_da3f097b], jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(
        self,
        value: typing.Union["CfnForm.FormDataTypeConfigProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7e19a017312460ae2a463321b8755f4cbb046f23e5b3f211bc3667291c8fc4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="fields")
    def fields(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnForm.FieldConfigProperty", _IResolvable_da3f097b]]]:
        '''``AWS::AmplifyUIBuilder::Form.Fields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-fields
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnForm.FieldConfigProperty", _IResolvable_da3f097b]]], jsii.get(self, "fields"))

    @fields.setter
    def fields(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnForm.FieldConfigProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9015687d91891d43612fe42019ff55cd0a88db183c4588c47c40ae844181ac0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fields", value)

    @builtins.property
    @jsii.member(jsii_name="formActionType")
    def form_action_type(self) -> builtins.str:
        '''``AWS::AmplifyUIBuilder::Form.FormActionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-formactiontype
        '''
        return typing.cast(builtins.str, jsii.get(self, "formActionType"))

    @form_action_type.setter
    def form_action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fc577f05ff38c0454a529f8e25d70043166c3c843ba386b8533d1566010fb3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "formActionType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::AmplifyUIBuilder::Form.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c37b5c0566194412a917f8b555c9713ff611891282349436c1825e2035304e0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schemaVersion")
    def schema_version(self) -> builtins.str:
        '''``AWS::AmplifyUIBuilder::Form.SchemaVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-schemaversion
        '''
        return typing.cast(builtins.str, jsii.get(self, "schemaVersion"))

    @schema_version.setter
    def schema_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__134b61ab92cc43448c72979bf06fe8c5b99e11026860e775bc799d1ac6f3485c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="sectionalElements")
    def sectional_elements(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnForm.SectionalElementProperty", _IResolvable_da3f097b]]]:
        '''``AWS::AmplifyUIBuilder::Form.SectionalElements``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-sectionalelements
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnForm.SectionalElementProperty", _IResolvable_da3f097b]]], jsii.get(self, "sectionalElements"))

    @sectional_elements.setter
    def sectional_elements(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnForm.SectionalElementProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85fa037be9d97ba3c80cd93837e11c8dbd4fe3a9d81a3b57bc62c3008fc0d045)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sectionalElements", value)

    @builtins.property
    @jsii.member(jsii_name="style")
    def style(self) -> typing.Union["CfnForm.FormStyleProperty", _IResolvable_da3f097b]:
        '''``AWS::AmplifyUIBuilder::Form.Style``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-style
        '''
        return typing.cast(typing.Union["CfnForm.FormStyleProperty", _IResolvable_da3f097b], jsii.get(self, "style"))

    @style.setter
    def style(
        self,
        value: typing.Union["CfnForm.FormStyleProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70860863c037915af307f857edb8d06dc079e810fc30f8a36441c45da0c1bed9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "style", value)

    @builtins.property
    @jsii.member(jsii_name="appId")
    def app_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::AmplifyUIBuilder::Form.AppId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-appid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appId"))

    @app_id.setter
    def app_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6086ddf273ace487109ec97dd1dc720c5f83ebbe24a96e2c42ae15646389d00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="cta")
    def cta(
        self,
    ) -> typing.Optional[typing.Union["CfnForm.FormCTAProperty", _IResolvable_da3f097b]]:
        '''``AWS::AmplifyUIBuilder::Form.Cta``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-cta
        '''
        return typing.cast(typing.Optional[typing.Union["CfnForm.FormCTAProperty", _IResolvable_da3f097b]], jsii.get(self, "cta"))

    @cta.setter
    def cta(
        self,
        value: typing.Optional[typing.Union["CfnForm.FormCTAProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcc01bb0df0b0a573caa23a9628b8cbfe2eb86510e0e390b92156dd05d486862)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cta", value)

    @builtins.property
    @jsii.member(jsii_name="environmentName")
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AmplifyUIBuilder::Form.EnvironmentName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-environmentname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentName"))

    @environment_name.setter
    def environment_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34caf84fc388835a97bc0ea839fd35da20c88a4c8e915204f78e924b66d4de02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.FieldConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "excluded": "excluded",
            "input_type": "inputType",
            "label": "label",
            "position": "position",
            "validations": "validations",
        },
    )
    class FieldConfigProperty:
        def __init__(
            self,
            *,
            excluded: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            input_type: typing.Optional[typing.Union[typing.Union["CfnForm.FieldInputConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            label: typing.Optional[builtins.str] = None,
            position: typing.Optional[typing.Union[typing.Union["CfnForm.FieldPositionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            validations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnForm.FieldValidationConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param excluded: ``CfnForm.FieldConfigProperty.Excluded``.
            :param input_type: ``CfnForm.FieldConfigProperty.InputType``.
            :param label: ``CfnForm.FieldConfigProperty.Label``.
            :param position: ``CfnForm.FieldConfigProperty.Position``.
            :param validations: ``CfnForm.FieldConfigProperty.Validations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                field_config_property = amplifyuibuilder.CfnForm.FieldConfigProperty(
                    excluded=False,
                    input_type=amplifyuibuilder.CfnForm.FieldInputConfigProperty(
                        type="type",
                
                        # the properties below are optional
                        default_checked=False,
                        default_country_code="defaultCountryCode",
                        default_value="defaultValue",
                        descriptive_text="descriptiveText",
                        max_value=123,
                        min_value=123,
                        name="name",
                        placeholder="placeholder",
                        read_only=False,
                        required=False,
                        step=123,
                        value="value",
                        value_mappings=amplifyuibuilder.CfnForm.ValueMappingsProperty(
                            values=[amplifyuibuilder.CfnForm.ValueMappingProperty(
                                value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                                    value="value"
                                ),
                
                                # the properties below are optional
                                display_value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                                    value="value"
                                )
                            )]
                        )
                    ),
                    label="label",
                    position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                        below="below",
                        fixed="fixed",
                        right_of="rightOf"
                    ),
                    validations=[amplifyuibuilder.CfnForm.FieldValidationConfigurationProperty(
                        type="type",
                
                        # the properties below are optional
                        num_values=[123],
                        str_values=["strValues"],
                        validation_message="validationMessage"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__facb12c1ebfafe4ee51a4282ac25081c6fb10fb0a82684aa169cb14fa6886efa)
                check_type(argname="argument excluded", value=excluded, expected_type=type_hints["excluded"])
                check_type(argname="argument input_type", value=input_type, expected_type=type_hints["input_type"])
                check_type(argname="argument label", value=label, expected_type=type_hints["label"])
                check_type(argname="argument position", value=position, expected_type=type_hints["position"])
                check_type(argname="argument validations", value=validations, expected_type=type_hints["validations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if excluded is not None:
                self._values["excluded"] = excluded
            if input_type is not None:
                self._values["input_type"] = input_type
            if label is not None:
                self._values["label"] = label
            if position is not None:
                self._values["position"] = position
            if validations is not None:
                self._values["validations"] = validations

        @builtins.property
        def excluded(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnForm.FieldConfigProperty.Excluded``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html#cfn-amplifyuibuilder-form-fieldconfig-excluded
            '''
            result = self._values.get("excluded")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def input_type(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FieldInputConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.FieldConfigProperty.InputType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html#cfn-amplifyuibuilder-form-fieldconfig-inputtype
            '''
            result = self._values.get("input_type")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FieldInputConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def label(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldConfigProperty.Label``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html#cfn-amplifyuibuilder-form-fieldconfig-label
            '''
            result = self._values.get("label")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def position(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FieldPositionProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.FieldConfigProperty.Position``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html#cfn-amplifyuibuilder-form-fieldconfig-position
            '''
            result = self._values.get("position")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FieldPositionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def validations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnForm.FieldValidationConfigurationProperty", _IResolvable_da3f097b]]]]:
            '''``CfnForm.FieldConfigProperty.Validations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html#cfn-amplifyuibuilder-form-fieldconfig-validations
            '''
            result = self._values.get("validations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnForm.FieldValidationConfigurationProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.FieldInputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "default_checked": "defaultChecked",
            "default_country_code": "defaultCountryCode",
            "default_value": "defaultValue",
            "descriptive_text": "descriptiveText",
            "max_value": "maxValue",
            "min_value": "minValue",
            "name": "name",
            "placeholder": "placeholder",
            "read_only": "readOnly",
            "required": "required",
            "step": "step",
            "value": "value",
            "value_mappings": "valueMappings",
        },
    )
    class FieldInputConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            default_checked: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            default_country_code: typing.Optional[builtins.str] = None,
            default_value: typing.Optional[builtins.str] = None,
            descriptive_text: typing.Optional[builtins.str] = None,
            max_value: typing.Optional[jsii.Number] = None,
            min_value: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
            placeholder: typing.Optional[builtins.str] = None,
            read_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            step: typing.Optional[jsii.Number] = None,
            value: typing.Optional[builtins.str] = None,
            value_mappings: typing.Optional[typing.Union[typing.Union["CfnForm.ValueMappingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param type: ``CfnForm.FieldInputConfigProperty.Type``.
            :param default_checked: ``CfnForm.FieldInputConfigProperty.DefaultChecked``.
            :param default_country_code: ``CfnForm.FieldInputConfigProperty.DefaultCountryCode``.
            :param default_value: ``CfnForm.FieldInputConfigProperty.DefaultValue``.
            :param descriptive_text: ``CfnForm.FieldInputConfigProperty.DescriptiveText``.
            :param max_value: ``CfnForm.FieldInputConfigProperty.MaxValue``.
            :param min_value: ``CfnForm.FieldInputConfigProperty.MinValue``.
            :param name: ``CfnForm.FieldInputConfigProperty.Name``.
            :param placeholder: ``CfnForm.FieldInputConfigProperty.Placeholder``.
            :param read_only: ``CfnForm.FieldInputConfigProperty.ReadOnly``.
            :param required: ``CfnForm.FieldInputConfigProperty.Required``.
            :param step: ``CfnForm.FieldInputConfigProperty.Step``.
            :param value: ``CfnForm.FieldInputConfigProperty.Value``.
            :param value_mappings: ``CfnForm.FieldInputConfigProperty.ValueMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                field_input_config_property = amplifyuibuilder.CfnForm.FieldInputConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    default_checked=False,
                    default_country_code="defaultCountryCode",
                    default_value="defaultValue",
                    descriptive_text="descriptiveText",
                    max_value=123,
                    min_value=123,
                    name="name",
                    placeholder="placeholder",
                    read_only=False,
                    required=False,
                    step=123,
                    value="value",
                    value_mappings=amplifyuibuilder.CfnForm.ValueMappingsProperty(
                        values=[amplifyuibuilder.CfnForm.ValueMappingProperty(
                            value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                                value="value"
                            ),
                
                            # the properties below are optional
                            display_value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                                value="value"
                            )
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2888e21dd850d2c3de4d4315337f2f5230a52e49287aa72328d2ad14617f64fa)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument default_checked", value=default_checked, expected_type=type_hints["default_checked"])
                check_type(argname="argument default_country_code", value=default_country_code, expected_type=type_hints["default_country_code"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument descriptive_text", value=descriptive_text, expected_type=type_hints["descriptive_text"])
                check_type(argname="argument max_value", value=max_value, expected_type=type_hints["max_value"])
                check_type(argname="argument min_value", value=min_value, expected_type=type_hints["min_value"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument placeholder", value=placeholder, expected_type=type_hints["placeholder"])
                check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
                check_type(argname="argument step", value=step, expected_type=type_hints["step"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument value_mappings", value=value_mappings, expected_type=type_hints["value_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if default_checked is not None:
                self._values["default_checked"] = default_checked
            if default_country_code is not None:
                self._values["default_country_code"] = default_country_code
            if default_value is not None:
                self._values["default_value"] = default_value
            if descriptive_text is not None:
                self._values["descriptive_text"] = descriptive_text
            if max_value is not None:
                self._values["max_value"] = max_value
            if min_value is not None:
                self._values["min_value"] = min_value
            if name is not None:
                self._values["name"] = name
            if placeholder is not None:
                self._values["placeholder"] = placeholder
            if read_only is not None:
                self._values["read_only"] = read_only
            if required is not None:
                self._values["required"] = required
            if step is not None:
                self._values["step"] = step
            if value is not None:
                self._values["value"] = value
            if value_mappings is not None:
                self._values["value_mappings"] = value_mappings

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnForm.FieldInputConfigProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def default_checked(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnForm.FieldInputConfigProperty.DefaultChecked``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-defaultchecked
            '''
            result = self._values.get("default_checked")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def default_country_code(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldInputConfigProperty.DefaultCountryCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-defaultcountrycode
            '''
            result = self._values.get("default_country_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldInputConfigProperty.DefaultValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def descriptive_text(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldInputConfigProperty.DescriptiveText``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-descriptivetext
            '''
            result = self._values.get("descriptive_text")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_value(self) -> typing.Optional[jsii.Number]:
            '''``CfnForm.FieldInputConfigProperty.MaxValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-maxvalue
            '''
            result = self._values.get("max_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_value(self) -> typing.Optional[jsii.Number]:
            '''``CfnForm.FieldInputConfigProperty.MinValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-minvalue
            '''
            result = self._values.get("min_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldInputConfigProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def placeholder(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldInputConfigProperty.Placeholder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-placeholder
            '''
            result = self._values.get("placeholder")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def read_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnForm.FieldInputConfigProperty.ReadOnly``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-readonly
            '''
            result = self._values.get("read_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnForm.FieldInputConfigProperty.Required``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-required
            '''
            result = self._values.get("required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def step(self) -> typing.Optional[jsii.Number]:
            '''``CfnForm.FieldInputConfigProperty.Step``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-step
            '''
            result = self._values.get("step")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldInputConfigProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value_mappings(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.ValueMappingsProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.FieldInputConfigProperty.ValueMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-valuemappings
            '''
            result = self._values.get("value_mappings")
            return typing.cast(typing.Optional[typing.Union["CfnForm.ValueMappingsProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldInputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.FieldPositionProperty",
        jsii_struct_bases=[],
        name_mapping={"below": "below", "fixed": "fixed", "right_of": "rightOf"},
    )
    class FieldPositionProperty:
        def __init__(
            self,
            *,
            below: typing.Optional[builtins.str] = None,
            fixed: typing.Optional[builtins.str] = None,
            right_of: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param below: ``CfnForm.FieldPositionProperty.Below``.
            :param fixed: ``CfnForm.FieldPositionProperty.Fixed``.
            :param right_of: ``CfnForm.FieldPositionProperty.RightOf``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                field_position_property = amplifyuibuilder.CfnForm.FieldPositionProperty(
                    below="below",
                    fixed="fixed",
                    right_of="rightOf"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__04a52fac39933b10d1cbbd03b00473e170b2984c315c7a3da3846dcc962e71c9)
                check_type(argname="argument below", value=below, expected_type=type_hints["below"])
                check_type(argname="argument fixed", value=fixed, expected_type=type_hints["fixed"])
                check_type(argname="argument right_of", value=right_of, expected_type=type_hints["right_of"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if below is not None:
                self._values["below"] = below
            if fixed is not None:
                self._values["fixed"] = fixed
            if right_of is not None:
                self._values["right_of"] = right_of

        @builtins.property
        def below(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldPositionProperty.Below``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html#cfn-amplifyuibuilder-form-fieldposition-below
            '''
            result = self._values.get("below")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fixed(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldPositionProperty.Fixed``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html#cfn-amplifyuibuilder-form-fieldposition-fixed
            '''
            result = self._values.get("fixed")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def right_of(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldPositionProperty.RightOf``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html#cfn-amplifyuibuilder-form-fieldposition-rightof
            '''
            result = self._values.get("right_of")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldPositionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.FieldValidationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "num_values": "numValues",
            "str_values": "strValues",
            "validation_message": "validationMessage",
        },
    )
    class FieldValidationConfigurationProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            num_values: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
            str_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            validation_message: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param type: ``CfnForm.FieldValidationConfigurationProperty.Type``.
            :param num_values: ``CfnForm.FieldValidationConfigurationProperty.NumValues``.
            :param str_values: ``CfnForm.FieldValidationConfigurationProperty.StrValues``.
            :param validation_message: ``CfnForm.FieldValidationConfigurationProperty.ValidationMessage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                field_validation_configuration_property = amplifyuibuilder.CfnForm.FieldValidationConfigurationProperty(
                    type="type",
                
                    # the properties below are optional
                    num_values=[123],
                    str_values=["strValues"],
                    validation_message="validationMessage"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__34136205c95f2f635b9e01e36902998c37a6de39668801b785b9506c14054296)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument num_values", value=num_values, expected_type=type_hints["num_values"])
                check_type(argname="argument str_values", value=str_values, expected_type=type_hints["str_values"])
                check_type(argname="argument validation_message", value=validation_message, expected_type=type_hints["validation_message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if num_values is not None:
                self._values["num_values"] = num_values
            if str_values is not None:
                self._values["str_values"] = str_values
            if validation_message is not None:
                self._values["validation_message"] = validation_message

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnForm.FieldValidationConfigurationProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def num_values(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]]:
            '''``CfnForm.FieldValidationConfigurationProperty.NumValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-numvalues
            '''
            result = self._values.get("num_values")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]], result)

        @builtins.property
        def str_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnForm.FieldValidationConfigurationProperty.StrValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-strvalues
            '''
            result = self._values.get("str_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def validation_message(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FieldValidationConfigurationProperty.ValidationMessage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-validationmessage
            '''
            result = self._values.get("validation_message")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldValidationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.FormButtonProperty",
        jsii_struct_bases=[],
        name_mapping={
            "children": "children",
            "excluded": "excluded",
            "position": "position",
        },
    )
    class FormButtonProperty:
        def __init__(
            self,
            *,
            children: typing.Optional[builtins.str] = None,
            excluded: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            position: typing.Optional[typing.Union[typing.Union["CfnForm.FieldPositionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param children: ``CfnForm.FormButtonProperty.Children``.
            :param excluded: ``CfnForm.FormButtonProperty.Excluded``.
            :param position: ``CfnForm.FormButtonProperty.Position``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                form_button_property = amplifyuibuilder.CfnForm.FormButtonProperty(
                    children="children",
                    excluded=False,
                    position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                        below="below",
                        fixed="fixed",
                        right_of="rightOf"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3aaebf617bf3553d285de51deaea2efd0785ae24ec5569ffb2d9a60d69da4425)
                check_type(argname="argument children", value=children, expected_type=type_hints["children"])
                check_type(argname="argument excluded", value=excluded, expected_type=type_hints["excluded"])
                check_type(argname="argument position", value=position, expected_type=type_hints["position"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if children is not None:
                self._values["children"] = children
            if excluded is not None:
                self._values["excluded"] = excluded
            if position is not None:
                self._values["position"] = position

        @builtins.property
        def children(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FormButtonProperty.Children``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html#cfn-amplifyuibuilder-form-formbutton-children
            '''
            result = self._values.get("children")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def excluded(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnForm.FormButtonProperty.Excluded``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html#cfn-amplifyuibuilder-form-formbutton-excluded
            '''
            result = self._values.get("excluded")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def position(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FieldPositionProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.FormButtonProperty.Position``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html#cfn-amplifyuibuilder-form-formbutton-position
            '''
            result = self._values.get("position")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FieldPositionProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormButtonProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.FormCTAProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cancel": "cancel",
            "clear": "clear",
            "position": "position",
            "submit": "submit",
        },
    )
    class FormCTAProperty:
        def __init__(
            self,
            *,
            cancel: typing.Optional[typing.Union[typing.Union["CfnForm.FormButtonProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            clear: typing.Optional[typing.Union[typing.Union["CfnForm.FormButtonProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            position: typing.Optional[builtins.str] = None,
            submit: typing.Optional[typing.Union[typing.Union["CfnForm.FormButtonProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param cancel: ``CfnForm.FormCTAProperty.Cancel``.
            :param clear: ``CfnForm.FormCTAProperty.Clear``.
            :param position: ``CfnForm.FormCTAProperty.Position``.
            :param submit: ``CfnForm.FormCTAProperty.Submit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                form_cTAProperty = amplifyuibuilder.CfnForm.FormCTAProperty(
                    cancel=amplifyuibuilder.CfnForm.FormButtonProperty(
                        children="children",
                        excluded=False,
                        position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                            below="below",
                            fixed="fixed",
                            right_of="rightOf"
                        )
                    ),
                    clear=amplifyuibuilder.CfnForm.FormButtonProperty(
                        children="children",
                        excluded=False,
                        position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                            below="below",
                            fixed="fixed",
                            right_of="rightOf"
                        )
                    ),
                    position="position",
                    submit=amplifyuibuilder.CfnForm.FormButtonProperty(
                        children="children",
                        excluded=False,
                        position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                            below="below",
                            fixed="fixed",
                            right_of="rightOf"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__77c752ecf91acd1ce1f6b4872c5597ec73be17115bab2a5f704d816a5af501d4)
                check_type(argname="argument cancel", value=cancel, expected_type=type_hints["cancel"])
                check_type(argname="argument clear", value=clear, expected_type=type_hints["clear"])
                check_type(argname="argument position", value=position, expected_type=type_hints["position"])
                check_type(argname="argument submit", value=submit, expected_type=type_hints["submit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cancel is not None:
                self._values["cancel"] = cancel
            if clear is not None:
                self._values["clear"] = clear
            if position is not None:
                self._values["position"] = position
            if submit is not None:
                self._values["submit"] = submit

        @builtins.property
        def cancel(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FormButtonProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.FormCTAProperty.Cancel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html#cfn-amplifyuibuilder-form-formcta-cancel
            '''
            result = self._values.get("cancel")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FormButtonProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def clear(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FormButtonProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.FormCTAProperty.Clear``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html#cfn-amplifyuibuilder-form-formcta-clear
            '''
            result = self._values.get("clear")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FormButtonProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def position(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FormCTAProperty.Position``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html#cfn-amplifyuibuilder-form-formcta-position
            '''
            result = self._values.get("position")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def submit(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FormButtonProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.FormCTAProperty.Submit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html#cfn-amplifyuibuilder-form-formcta-submit
            '''
            result = self._values.get("submit")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FormButtonProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormCTAProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.FormDataTypeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_type": "dataSourceType",
            "data_type_name": "dataTypeName",
        },
    )
    class FormDataTypeConfigProperty:
        def __init__(
            self,
            *,
            data_source_type: builtins.str,
            data_type_name: builtins.str,
        ) -> None:
            '''
            :param data_source_type: ``CfnForm.FormDataTypeConfigProperty.DataSourceType``.
            :param data_type_name: ``CfnForm.FormDataTypeConfigProperty.DataTypeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formdatatypeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                form_data_type_config_property = amplifyuibuilder.CfnForm.FormDataTypeConfigProperty(
                    data_source_type="dataSourceType",
                    data_type_name="dataTypeName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c13c26fc166a4f957568be30eae909c624b75f8f8139e0588fece7eeee3282ae)
                check_type(argname="argument data_source_type", value=data_source_type, expected_type=type_hints["data_source_type"])
                check_type(argname="argument data_type_name", value=data_type_name, expected_type=type_hints["data_type_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_source_type": data_source_type,
                "data_type_name": data_type_name,
            }

        @builtins.property
        def data_source_type(self) -> builtins.str:
            '''``CfnForm.FormDataTypeConfigProperty.DataSourceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formdatatypeconfig.html#cfn-amplifyuibuilder-form-formdatatypeconfig-datasourcetype
            '''
            result = self._values.get("data_source_type")
            assert result is not None, "Required property 'data_source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_type_name(self) -> builtins.str:
            '''``CfnForm.FormDataTypeConfigProperty.DataTypeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formdatatypeconfig.html#cfn-amplifyuibuilder-form-formdatatypeconfig-datatypename
            '''
            result = self._values.get("data_type_name")
            assert result is not None, "Required property 'data_type_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormDataTypeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.FormInputValuePropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class FormInputValuePropertyProperty:
        def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
            '''
            :param value: ``CfnForm.FormInputValuePropertyProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-forminputvalueproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                form_input_value_property_property = amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__18fb1cc6c981a6a2bd1a5b53248a9d11f4a7c98e09a7132c1a7ca82bcd56c726)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FormInputValuePropertyProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-forminputvalueproperty.html#cfn-amplifyuibuilder-form-forminputvalueproperty-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormInputValuePropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.FormStyleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"token_reference": "tokenReference", "value": "value"},
    )
    class FormStyleConfigProperty:
        def __init__(
            self,
            *,
            token_reference: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param token_reference: ``CfnForm.FormStyleConfigProperty.TokenReference``.
            :param value: ``CfnForm.FormStyleConfigProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyleconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                form_style_config_property = amplifyuibuilder.CfnForm.FormStyleConfigProperty(
                    token_reference="tokenReference",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2eee01779eb429842d3c379bc94ce33ffc0e13bb071fc183cfbefbf30d80f6b8)
                check_type(argname="argument token_reference", value=token_reference, expected_type=type_hints["token_reference"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if token_reference is not None:
                self._values["token_reference"] = token_reference
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def token_reference(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FormStyleConfigProperty.TokenReference``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyleconfig.html#cfn-amplifyuibuilder-form-formstyleconfig-tokenreference
            '''
            result = self._values.get("token_reference")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.FormStyleConfigProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyleconfig.html#cfn-amplifyuibuilder-form-formstyleconfig-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormStyleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.FormStyleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "horizontal_gap": "horizontalGap",
            "outer_padding": "outerPadding",
            "vertical_gap": "verticalGap",
        },
    )
    class FormStyleProperty:
        def __init__(
            self,
            *,
            horizontal_gap: typing.Optional[typing.Union[typing.Union["CfnForm.FormStyleConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            outer_padding: typing.Optional[typing.Union[typing.Union["CfnForm.FormStyleConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            vertical_gap: typing.Optional[typing.Union[typing.Union["CfnForm.FormStyleConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param horizontal_gap: ``CfnForm.FormStyleProperty.HorizontalGap``.
            :param outer_padding: ``CfnForm.FormStyleProperty.OuterPadding``.
            :param vertical_gap: ``CfnForm.FormStyleProperty.VerticalGap``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                form_style_property = amplifyuibuilder.CfnForm.FormStyleProperty(
                    horizontal_gap=amplifyuibuilder.CfnForm.FormStyleConfigProperty(
                        token_reference="tokenReference",
                        value="value"
                    ),
                    outer_padding=amplifyuibuilder.CfnForm.FormStyleConfigProperty(
                        token_reference="tokenReference",
                        value="value"
                    ),
                    vertical_gap=amplifyuibuilder.CfnForm.FormStyleConfigProperty(
                        token_reference="tokenReference",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__50be8c564fec3c46684431a761d27d986411251dd2dbff52def67a46d2b37f76)
                check_type(argname="argument horizontal_gap", value=horizontal_gap, expected_type=type_hints["horizontal_gap"])
                check_type(argname="argument outer_padding", value=outer_padding, expected_type=type_hints["outer_padding"])
                check_type(argname="argument vertical_gap", value=vertical_gap, expected_type=type_hints["vertical_gap"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if horizontal_gap is not None:
                self._values["horizontal_gap"] = horizontal_gap
            if outer_padding is not None:
                self._values["outer_padding"] = outer_padding
            if vertical_gap is not None:
                self._values["vertical_gap"] = vertical_gap

        @builtins.property
        def horizontal_gap(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FormStyleConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.FormStyleProperty.HorizontalGap``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html#cfn-amplifyuibuilder-form-formstyle-horizontalgap
            '''
            result = self._values.get("horizontal_gap")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FormStyleConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def outer_padding(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FormStyleConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.FormStyleProperty.OuterPadding``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html#cfn-amplifyuibuilder-form-formstyle-outerpadding
            '''
            result = self._values.get("outer_padding")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FormStyleConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def vertical_gap(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FormStyleConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.FormStyleProperty.VerticalGap``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html#cfn-amplifyuibuilder-form-formstyle-verticalgap
            '''
            result = self._values.get("vertical_gap")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FormStyleConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.SectionalElementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "level": "level",
            "orientation": "orientation",
            "position": "position",
            "text": "text",
        },
    )
    class SectionalElementProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            level: typing.Optional[jsii.Number] = None,
            orientation: typing.Optional[builtins.str] = None,
            position: typing.Optional[typing.Union[typing.Union["CfnForm.FieldPositionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            text: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param type: ``CfnForm.SectionalElementProperty.Type``.
            :param level: ``CfnForm.SectionalElementProperty.Level``.
            :param orientation: ``CfnForm.SectionalElementProperty.Orientation``.
            :param position: ``CfnForm.SectionalElementProperty.Position``.
            :param text: ``CfnForm.SectionalElementProperty.Text``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                sectional_element_property = amplifyuibuilder.CfnForm.SectionalElementProperty(
                    type="type",
                
                    # the properties below are optional
                    level=123,
                    orientation="orientation",
                    position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                        below="below",
                        fixed="fixed",
                        right_of="rightOf"
                    ),
                    text="text"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__de6d8665fe6651d5620544536ddb9794f1f75f8f980fd73240f5d8c373dec173)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument level", value=level, expected_type=type_hints["level"])
                check_type(argname="argument orientation", value=orientation, expected_type=type_hints["orientation"])
                check_type(argname="argument position", value=position, expected_type=type_hints["position"])
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if level is not None:
                self._values["level"] = level
            if orientation is not None:
                self._values["orientation"] = orientation
            if position is not None:
                self._values["position"] = position
            if text is not None:
                self._values["text"] = text

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnForm.SectionalElementProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def level(self) -> typing.Optional[jsii.Number]:
            '''``CfnForm.SectionalElementProperty.Level``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-level
            '''
            result = self._values.get("level")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def orientation(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.SectionalElementProperty.Orientation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-orientation
            '''
            result = self._values.get("orientation")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def position(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FieldPositionProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.SectionalElementProperty.Position``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-position
            '''
            result = self._values.get("position")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FieldPositionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def text(self) -> typing.Optional[builtins.str]:
            '''``CfnForm.SectionalElementProperty.Text``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-text
            '''
            result = self._values.get("text")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SectionalElementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.ValueMappingProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "display_value": "displayValue"},
    )
    class ValueMappingProperty:
        def __init__(
            self,
            *,
            value: typing.Union[typing.Union["CfnForm.FormInputValuePropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
            display_value: typing.Optional[typing.Union[typing.Union["CfnForm.FormInputValuePropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param value: ``CfnForm.ValueMappingProperty.Value``.
            :param display_value: ``CfnForm.ValueMappingProperty.DisplayValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                value_mapping_property = amplifyuibuilder.CfnForm.ValueMappingProperty(
                    value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                        value="value"
                    ),
                
                    # the properties below are optional
                    display_value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e5a419a9779cbf833c1ce04bf2e120ab8acfe6226e2a461b0e4f2dce065c4c1b)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument display_value", value=display_value, expected_type=type_hints["display_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }
            if display_value is not None:
                self._values["display_value"] = display_value

        @builtins.property
        def value(
            self,
        ) -> typing.Union["CfnForm.FormInputValuePropertyProperty", _IResolvable_da3f097b]:
            '''``CfnForm.ValueMappingProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemapping.html#cfn-amplifyuibuilder-form-valuemapping-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union["CfnForm.FormInputValuePropertyProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def display_value(
            self,
        ) -> typing.Optional[typing.Union["CfnForm.FormInputValuePropertyProperty", _IResolvable_da3f097b]]:
            '''``CfnForm.ValueMappingProperty.DisplayValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemapping.html#cfn-amplifyuibuilder-form-valuemapping-displayvalue
            '''
            result = self._values.get("display_value")
            return typing.cast(typing.Optional[typing.Union["CfnForm.FormInputValuePropertyProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValueMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnForm.ValueMappingsProperty",
        jsii_struct_bases=[],
        name_mapping={"values": "values"},
    )
    class ValueMappingsProperty:
        def __init__(
            self,
            *,
            values: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnForm.ValueMappingProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        ) -> None:
            '''
            :param values: ``CfnForm.ValueMappingsProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemappings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                value_mappings_property = amplifyuibuilder.CfnForm.ValueMappingsProperty(
                    values=[amplifyuibuilder.CfnForm.ValueMappingProperty(
                        value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                            value="value"
                        ),
                
                        # the properties below are optional
                        display_value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                            value="value"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d724ce98e4e33046526453a6db65965e6f336a8f4ff6e0f67b70823d84267d95)
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "values": values,
            }

        @builtins.property
        def values(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnForm.ValueMappingProperty", _IResolvable_da3f097b]]]:
            '''``CfnForm.ValueMappingsProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemappings.html#cfn-amplifyuibuilder-form-valuemappings-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnForm.ValueMappingProperty", _IResolvable_da3f097b]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValueMappingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnFormProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_type": "dataType",
        "fields": "fields",
        "form_action_type": "formActionType",
        "name": "name",
        "schema_version": "schemaVersion",
        "sectional_elements": "sectionalElements",
        "style": "style",
        "app_id": "appId",
        "cta": "cta",
        "environment_name": "environmentName",
        "tags": "tags",
    },
)
class CfnFormProps:
    def __init__(
        self,
        *,
        data_type: typing.Union[typing.Union[CfnForm.FormDataTypeConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        fields: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnForm.FieldConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        form_action_type: builtins.str,
        name: builtins.str,
        schema_version: builtins.str,
        sectional_elements: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnForm.SectionalElementProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        style: typing.Union[typing.Union[CfnForm.FormStyleProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        app_id: typing.Optional[builtins.str] = None,
        cta: typing.Optional[typing.Union[typing.Union[CfnForm.FormCTAProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        environment_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnForm``.

        :param data_type: ``AWS::AmplifyUIBuilder::Form.DataType``.
        :param fields: ``AWS::AmplifyUIBuilder::Form.Fields``.
        :param form_action_type: ``AWS::AmplifyUIBuilder::Form.FormActionType``.
        :param name: ``AWS::AmplifyUIBuilder::Form.Name``.
        :param schema_version: ``AWS::AmplifyUIBuilder::Form.SchemaVersion``.
        :param sectional_elements: ``AWS::AmplifyUIBuilder::Form.SectionalElements``.
        :param style: ``AWS::AmplifyUIBuilder::Form.Style``.
        :param app_id: ``AWS::AmplifyUIBuilder::Form.AppId``.
        :param cta: ``AWS::AmplifyUIBuilder::Form.Cta``.
        :param environment_name: ``AWS::AmplifyUIBuilder::Form.EnvironmentName``.
        :param tags: ``AWS::AmplifyUIBuilder::Form.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
            
            cfn_form_props = amplifyuibuilder.CfnFormProps(
                data_type=amplifyuibuilder.CfnForm.FormDataTypeConfigProperty(
                    data_source_type="dataSourceType",
                    data_type_name="dataTypeName"
                ),
                fields={
                    "fields_key": amplifyuibuilder.CfnForm.FieldConfigProperty(
                        excluded=False,
                        input_type=amplifyuibuilder.CfnForm.FieldInputConfigProperty(
                            type="type",
            
                            # the properties below are optional
                            default_checked=False,
                            default_country_code="defaultCountryCode",
                            default_value="defaultValue",
                            descriptive_text="descriptiveText",
                            max_value=123,
                            min_value=123,
                            name="name",
                            placeholder="placeholder",
                            read_only=False,
                            required=False,
                            step=123,
                            value="value",
                            value_mappings=amplifyuibuilder.CfnForm.ValueMappingsProperty(
                                values=[amplifyuibuilder.CfnForm.ValueMappingProperty(
                                    value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                                        value="value"
                                    ),
            
                                    # the properties below are optional
                                    display_value=amplifyuibuilder.CfnForm.FormInputValuePropertyProperty(
                                        value="value"
                                    )
                                )]
                            )
                        ),
                        label="label",
                        position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                            below="below",
                            fixed="fixed",
                            right_of="rightOf"
                        ),
                        validations=[amplifyuibuilder.CfnForm.FieldValidationConfigurationProperty(
                            type="type",
            
                            # the properties below are optional
                            num_values=[123],
                            str_values=["strValues"],
                            validation_message="validationMessage"
                        )]
                    )
                },
                form_action_type="formActionType",
                name="name",
                schema_version="schemaVersion",
                sectional_elements={
                    "sectional_elements_key": amplifyuibuilder.CfnForm.SectionalElementProperty(
                        type="type",
            
                        # the properties below are optional
                        level=123,
                        orientation="orientation",
                        position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                            below="below",
                            fixed="fixed",
                            right_of="rightOf"
                        ),
                        text="text"
                    )
                },
                style=amplifyuibuilder.CfnForm.FormStyleProperty(
                    horizontal_gap=amplifyuibuilder.CfnForm.FormStyleConfigProperty(
                        token_reference="tokenReference",
                        value="value"
                    ),
                    outer_padding=amplifyuibuilder.CfnForm.FormStyleConfigProperty(
                        token_reference="tokenReference",
                        value="value"
                    ),
                    vertical_gap=amplifyuibuilder.CfnForm.FormStyleConfigProperty(
                        token_reference="tokenReference",
                        value="value"
                    )
                ),
            
                # the properties below are optional
                app_id="appId",
                cta=amplifyuibuilder.CfnForm.FormCTAProperty(
                    cancel=amplifyuibuilder.CfnForm.FormButtonProperty(
                        children="children",
                        excluded=False,
                        position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                            below="below",
                            fixed="fixed",
                            right_of="rightOf"
                        )
                    ),
                    clear=amplifyuibuilder.CfnForm.FormButtonProperty(
                        children="children",
                        excluded=False,
                        position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                            below="below",
                            fixed="fixed",
                            right_of="rightOf"
                        )
                    ),
                    position="position",
                    submit=amplifyuibuilder.CfnForm.FormButtonProperty(
                        children="children",
                        excluded=False,
                        position=amplifyuibuilder.CfnForm.FieldPositionProperty(
                            below="below",
                            fixed="fixed",
                            right_of="rightOf"
                        )
                    )
                ),
                environment_name="environmentName",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bb63d5cc6b32485abf45108b28446e1c750de14c1855dae86134a9765f5dbf4)
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument form_action_type", value=form_action_type, expected_type=type_hints["form_action_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema_version", value=schema_version, expected_type=type_hints["schema_version"])
            check_type(argname="argument sectional_elements", value=sectional_elements, expected_type=type_hints["sectional_elements"])
            check_type(argname="argument style", value=style, expected_type=type_hints["style"])
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
            check_type(argname="argument cta", value=cta, expected_type=type_hints["cta"])
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_type": data_type,
            "fields": fields,
            "form_action_type": form_action_type,
            "name": name,
            "schema_version": schema_version,
            "sectional_elements": sectional_elements,
            "style": style,
        }
        if app_id is not None:
            self._values["app_id"] = app_id
        if cta is not None:
            self._values["cta"] = cta
        if environment_name is not None:
            self._values["environment_name"] = environment_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_type(
        self,
    ) -> typing.Union[CfnForm.FormDataTypeConfigProperty, _IResolvable_da3f097b]:
        '''``AWS::AmplifyUIBuilder::Form.DataType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-datatype
        '''
        result = self._values.get("data_type")
        assert result is not None, "Required property 'data_type' is missing"
        return typing.cast(typing.Union[CfnForm.FormDataTypeConfigProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def fields(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnForm.FieldConfigProperty, _IResolvable_da3f097b]]]:
        '''``AWS::AmplifyUIBuilder::Form.Fields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-fields
        '''
        result = self._values.get("fields")
        assert result is not None, "Required property 'fields' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnForm.FieldConfigProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def form_action_type(self) -> builtins.str:
        '''``AWS::AmplifyUIBuilder::Form.FormActionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-formactiontype
        '''
        result = self._values.get("form_action_type")
        assert result is not None, "Required property 'form_action_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::AmplifyUIBuilder::Form.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_version(self) -> builtins.str:
        '''``AWS::AmplifyUIBuilder::Form.SchemaVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-schemaversion
        '''
        result = self._values.get("schema_version")
        assert result is not None, "Required property 'schema_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sectional_elements(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnForm.SectionalElementProperty, _IResolvable_da3f097b]]]:
        '''``AWS::AmplifyUIBuilder::Form.SectionalElements``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-sectionalelements
        '''
        result = self._values.get("sectional_elements")
        assert result is not None, "Required property 'sectional_elements' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnForm.SectionalElementProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def style(self) -> typing.Union[CfnForm.FormStyleProperty, _IResolvable_da3f097b]:
        '''``AWS::AmplifyUIBuilder::Form.Style``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-style
        '''
        result = self._values.get("style")
        assert result is not None, "Required property 'style' is missing"
        return typing.cast(typing.Union[CfnForm.FormStyleProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def app_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::AmplifyUIBuilder::Form.AppId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-appid
        '''
        result = self._values.get("app_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cta(
        self,
    ) -> typing.Optional[typing.Union[CfnForm.FormCTAProperty, _IResolvable_da3f097b]]:
        '''``AWS::AmplifyUIBuilder::Form.Cta``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-cta
        '''
        result = self._values.get("cta")
        return typing.cast(typing.Optional[typing.Union[CfnForm.FormCTAProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AmplifyUIBuilder::Form.EnvironmentName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-environmentname
        '''
        result = self._values.get("environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::AmplifyUIBuilder::Form.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFormProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTheme(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnTheme",
):
    '''A CloudFormation ``AWS::AmplifyUIBuilder::Theme``.

    The AWS::AmplifyUIBuilder::Theme resource specifies a theme within an Amplify app. A theme is a collection of style settings that apply globally to the components associated with the app.

    :cloudformationResource: AWS::AmplifyUIBuilder::Theme
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
        
        # theme_values_property_: amplifyuibuilder.CfnTheme.ThemeValuesProperty
        
        cfn_theme = amplifyuibuilder.CfnTheme(self, "MyCfnTheme",
            name="name",
            values=[amplifyuibuilder.CfnTheme.ThemeValuesProperty(
                key="key",
                value=amplifyuibuilder.CfnTheme.ThemeValueProperty(
                    children=[theme_values_property_],
                    value="value"
                )
            )],
        
            # the properties below are optional
            overrides=[amplifyuibuilder.CfnTheme.ThemeValuesProperty(
                key="key",
                value=amplifyuibuilder.CfnTheme.ThemeValueProperty(
                    children=[theme_values_property_],
                    value="value"
                )
            )],
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        values: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTheme.ThemeValuesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTheme.ThemeValuesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::AmplifyUIBuilder::Theme``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the theme.
        :param values: A list of key-value pairs that defines the properties of the theme.
        :param overrides: Describes the properties that can be overriden to customize a theme.
        :param tags: One or more key-value pairs to use when tagging the theme.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2279f682c519f8cd82b48b2513abcff891e39a55368285f7ff433a9378321040)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnThemeProps(name=name, values=values, overrides=overrides, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab465f089075b33a373e16d0ddf12b8c4ce3438c656f46db2c8ac0ac15208a34)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a229aebaa77e6195b91d905366ce47f16aebf09185cd76886e729ba2b05c685)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAppId")
    def attr_app_id(self) -> builtins.str:
        '''The unique ID for the Amplify app associated with the theme.

        :cloudformationAttribute: AppId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time that the theme was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentName")
    def attr_environment_name(self) -> builtins.str:
        '''The name of the backend environment that is a part of the Amplify app.

        :cloudformationAttribute: EnvironmentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentName"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID for the theme.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''The time that the theme was modified.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''One or more key-value pairs to use when tagging the theme.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the theme.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37420262c86d20249895865fc6efbd1cf14792658f7f10af8ab3410f125160d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTheme.ThemeValuesProperty", _IResolvable_da3f097b]]]:
        '''A list of key-value pairs that defines the properties of the theme.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-values
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTheme.ThemeValuesProperty", _IResolvable_da3f097b]]], jsii.get(self, "values"))

    @values.setter
    def values(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTheme.ThemeValuesProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb8701acac3d1216eee5ea6afa5963493d323823cf518c1ba70eebb677f169f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="overrides")
    def overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTheme.ThemeValuesProperty", _IResolvable_da3f097b]]]]:
        '''Describes the properties that can be overriden to customize a theme.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-overrides
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTheme.ThemeValuesProperty", _IResolvable_da3f097b]]]], jsii.get(self, "overrides"))

    @overrides.setter
    def overrides(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTheme.ThemeValuesProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__447d8cae12df687b1981d85cd7ad953ecb265c415202fa332bdb6ac0bdbc8d7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrides", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnTheme.ThemeValueProperty",
        jsii_struct_bases=[],
        name_mapping={"children": "children", "value": "value"},
    )
    class ThemeValueProperty:
        def __init__(
            self,
            *,
            children: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTheme.ThemeValuesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``ThemeValue`` property specifies the configuration of a theme's properties.

            :param children: A list of key-value pairs that define the theme's properties.
            :param value: The value of a theme property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # theme_values_property_: amplifyuibuilder.CfnTheme.ThemeValuesProperty
                
                theme_value_property = amplifyuibuilder.CfnTheme.ThemeValueProperty(
                    children=[amplifyuibuilder.CfnTheme.ThemeValuesProperty(
                        key="key",
                        value=amplifyuibuilder.CfnTheme.ThemeValueProperty(
                            children=[theme_values_property_],
                            value="value"
                        )
                    )],
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__968a2203f12b6fe147c86388655984948ce554ab590d84eab56303a5cb4f1443)
                check_type(argname="argument children", value=children, expected_type=type_hints["children"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if children is not None:
                self._values["children"] = children
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def children(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTheme.ThemeValuesProperty", _IResolvable_da3f097b]]]]:
            '''A list of key-value pairs that define the theme's properties.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalue.html#cfn-amplifyuibuilder-theme-themevalue-children
            '''
            result = self._values.get("children")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTheme.ThemeValuesProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of a theme property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalue.html#cfn-amplifyuibuilder-theme-themevalue-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThemeValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnTheme.ThemeValuesProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ThemeValuesProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[typing.Union[typing.Union["CfnTheme.ThemeValueProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``ThemeValues`` property specifies key-value pair that defines a property of a theme.

            :param key: The name of the property.
            :param value: The value of the property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalues.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
                
                # theme_value_property_: amplifyuibuilder.CfnTheme.ThemeValueProperty
                
                theme_values_property = amplifyuibuilder.CfnTheme.ThemeValuesProperty(
                    key="key",
                    value=amplifyuibuilder.CfnTheme.ThemeValueProperty(
                        children=[amplifyuibuilder.CfnTheme.ThemeValuesProperty(
                            key="key",
                            value=theme_value_property_
                        )],
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__32916eb6e9dca0f7a126b89c19d4efd2943a6c491612af96a25d95ebbc0772d4)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The name of the property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalues.html#cfn-amplifyuibuilder-theme-themevalues-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.ThemeValueProperty", _IResolvable_da3f097b]]:
            '''The value of the property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalues.html#cfn-amplifyuibuilder-theme-themevalues-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[typing.Union["CfnTheme.ThemeValueProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThemeValuesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_amplifyuibuilder.CfnThemeProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "values": "values",
        "overrides": "overrides",
        "tags": "tags",
    },
)
class CfnThemeProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnTheme.ThemeValuesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
        overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnTheme.ThemeValuesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTheme``.

        :param name: The name of the theme.
        :param values: A list of key-value pairs that defines the properties of the theme.
        :param overrides: Describes the properties that can be overriden to customize a theme.
        :param tags: One or more key-value pairs to use when tagging the theme.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_amplifyuibuilder as amplifyuibuilder
            
            # theme_values_property_: amplifyuibuilder.CfnTheme.ThemeValuesProperty
            
            cfn_theme_props = amplifyuibuilder.CfnThemeProps(
                name="name",
                values=[amplifyuibuilder.CfnTheme.ThemeValuesProperty(
                    key="key",
                    value=amplifyuibuilder.CfnTheme.ThemeValueProperty(
                        children=[theme_values_property_],
                        value="value"
                    )
                )],
            
                # the properties below are optional
                overrides=[amplifyuibuilder.CfnTheme.ThemeValuesProperty(
                    key="key",
                    value=amplifyuibuilder.CfnTheme.ThemeValueProperty(
                        children=[theme_values_property_],
                        value="value"
                    )
                )],
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77360f99c7978648939d69b66977b92aefcb6819d200949e380c72c121fb7bad)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "values": values,
        }
        if overrides is not None:
            self._values["overrides"] = overrides
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the theme.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTheme.ThemeValuesProperty, _IResolvable_da3f097b]]]:
        '''A list of key-value pairs that defines the properties of the theme.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-values
        '''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTheme.ThemeValuesProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTheme.ThemeValuesProperty, _IResolvable_da3f097b]]]]:
        '''Describes the properties that can be overriden to customize a theme.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-overrides
        '''
        result = self._values.get("overrides")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTheme.ThemeValuesProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''One or more key-value pairs to use when tagging the theme.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThemeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnComponent",
    "CfnComponentProps",
    "CfnForm",
    "CfnFormProps",
    "CfnTheme",
    "CfnThemeProps",
]

publication.publish()

def _typecheckingstub__fd7799829199faf127a94fa77781fc238076f764c5a29e3192b18302477d99ad(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    binding_properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentBindingPropertiesValueProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    component_type: builtins.str,
    name: builtins.str,
    overrides: typing.Any,
    properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    variants: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.ComponentVariantProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    children: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.ComponentChildProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    collection_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentDataConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentEventProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    schema_version: typing.Optional[builtins.str] = None,
    source_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a4071d72b1c192773d27cf1393fcd31a209b8da1710b4cc3887aaa640711a2b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5845dbb422dcf82315243e4c81979c1db599d6f4e807c7e8d29cce12a0123aba(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4318ac16b5fec407f318eecf547fbef09f6a25d44eee663a0eb2d9d4cfb515c8(
    value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentBindingPropertiesValueProperty, _IResolvable_da3f097b]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d75568dbcc6cfcf6d654bc9d347cea6e2a04e9fed153e3f59a35fd309d097273(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d390004d0f30759542ef28ada1804bcce6e8abbebac682bdb562339425f06133(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0df3bcfbc7a5f3b8c1c149ff6cbac150b1f0b40f2b39df29eaf014b9a94c7083(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__996d9ae7924c5b47d79b0dc8a0bdd64fe013219ccbe4230a2423b7e9ad5aba37(
    value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentPropertyProperty, _IResolvable_da3f097b]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21622fc70206995803294c972e78d130850c0e1dde7f836f2646dd47d873fc48(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnComponent.ComponentVariantProperty, _IResolvable_da3f097b]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc8d6f7afd78df5a6542a7697bbb32d8d2c9e5a18e80e3386de082f4e2b7071(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnComponent.ComponentChildProperty, _IResolvable_da3f097b]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ccd617dfcaf796edb26a70160a96d7ac3771afa99ba8a4500e7927f724ee8d2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentDataConfigurationProperty, _IResolvable_da3f097b]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867f4afaa52290132593733e3be70d110a540505523ee1a4b0bea23f5a059f8c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnComponent.ComponentEventProperty, _IResolvable_da3f097b]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cce35ca7f734518c2d5b6c459ad169208cc7c4b0e7c4955205c3b6e4bdc8f484(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1265b5d410f7cdf2344a649e0fe6921e9ffd6d7c60569ba0b37eedfeea753d74(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__396df9c0159ef2683a2d199aa0e6b6baece439a466a700800ddc5e140dd124b1(
    *,
    anchor: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    global_: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    id: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    model: typing.Optional[builtins.str] = None,
    state: typing.Optional[typing.Union[typing.Union[CfnComponent.MutationActionSetStateParameterProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    target: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    type: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    url: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81ff632b19dd9fd8d12fdc9b6929e5e551d79797cb14dd1ca0cf7644998a657c(
    *,
    bucket: typing.Optional[builtins.str] = None,
    default_value: typing.Optional[builtins.str] = None,
    field: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    model: typing.Optional[builtins.str] = None,
    predicates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.PredicateProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    user_attribute: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff7030ae0aef39d7f52ec52503b8ffe4b3b2f9eab3ec5a0b307d62df215fac00(
    *,
    binding_properties: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentBindingPropertiesValuePropertiesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    default_value: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3d50eae10e05ec6519c8b5405904b780a7f01613f52ff55abfb41b0c9edc884(
    *,
    component_type: builtins.str,
    name: builtins.str,
    properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    children: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.ComponentChildProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentEventProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a087a026a105fe370e8b30547f8deb28449cbbc0ea16d6168c3ffe40b9fc3f7(
    *,
    else_: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    field: typing.Optional[builtins.str] = None,
    operand: typing.Optional[builtins.str] = None,
    operand_type: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    property: typing.Optional[builtins.str] = None,
    then: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64e141d7e4f47c6e1581f7d74ffea218f473c3420b88087f34835976ebac771f(
    *,
    model: builtins.str,
    identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
    predicate: typing.Optional[typing.Union[typing.Union[CfnComponent.PredicateProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    sort: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.SortPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a2199271a6b5de84d37a061bced7624cc98fc5b38d9799e48008b25cc4beb30(
    *,
    action: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[typing.Union[CfnComponent.ActionParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6609f397f447132bed1b4dae768619a73958cd6fb765edd0f7a2623013c57096(
    *,
    property: builtins.str,
    field: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cf7d407c19a13b1e358d52a06851a4288f7e5e365289ff8c22d9b2d67d8d179(
    *,
    binding_properties: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentPropertyBindingPropertiesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    bindings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.FormBindingElementProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    collection_binding_properties: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentPropertyBindingPropertiesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    component_name: typing.Optional[builtins.str] = None,
    concat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    condition: typing.Optional[typing.Union[typing.Union[CfnComponent.ComponentConditionPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    configured: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    default_value: typing.Optional[builtins.str] = None,
    event: typing.Optional[builtins.str] = None,
    imported_value: typing.Optional[builtins.str] = None,
    model: typing.Optional[builtins.str] = None,
    property: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    user_attribute: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__295e4045520d86ca93a4865404c10aafdb49dd91806c9cae31545fdd54e9bee9(
    *,
    overrides: typing.Any = None,
    variant_values: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__083b2206ecf6efde86ba8aefa3608c36f293532c3f9ff7e1ec5724b9f2540d0a(
    *,
    element: builtins.str,
    property: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c7bf8adc174a1333d4f6712bb6a171a89b27809627e9e7265e3d111f78189a(
    *,
    component_name: builtins.str,
    property: builtins.str,
    set: typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37ce81ce3ae3ad1d19dadf5542dca7cb3465cd10747b81f17e473f6a27342336(
    *,
    and_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.PredicateProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    field: typing.Optional[builtins.str] = None,
    operand: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    or_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.PredicateProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e28aa12f1ac083d97c2507afcccfed6130be39825a273208c629b58a9826c9d(
    *,
    direction: builtins.str,
    field: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f53200a7ca068c25e3052be6f1490d18f9816b65f2cfec3a854a23ba3d5e5f45(
    *,
    binding_properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentBindingPropertiesValueProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    component_type: builtins.str,
    name: builtins.str,
    overrides: typing.Any,
    properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    variants: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.ComponentVariantProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    children: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnComponent.ComponentChildProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    collection_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentDataConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnComponent.ComponentEventProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    schema_version: typing.Optional[builtins.str] = None,
    source_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1e1e67668c27ec66bb2b6aa2fd792ed1f3347990281e8dd83ae2ac8e81aaac8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_type: typing.Union[typing.Union[CfnForm.FormDataTypeConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    fields: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnForm.FieldConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    form_action_type: builtins.str,
    name: builtins.str,
    schema_version: builtins.str,
    sectional_elements: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnForm.SectionalElementProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    style: typing.Union[typing.Union[CfnForm.FormStyleProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    app_id: typing.Optional[builtins.str] = None,
    cta: typing.Optional[typing.Union[typing.Union[CfnForm.FormCTAProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    environment_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c21e8cabf9d014e4b7da846798df9ed12d78b23e1e4bc708e80a16526466e109(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8dedc67622f4e478423a2acbe47f789044cbf9bf399c9f14ba25932fda2994e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7e19a017312460ae2a463321b8755f4cbb046f23e5b3f211bc3667291c8fc4c(
    value: typing.Union[CfnForm.FormDataTypeConfigProperty, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9015687d91891d43612fe42019ff55cd0a88db183c4588c47c40ae844181ac0(
    value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnForm.FieldConfigProperty, _IResolvable_da3f097b]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fc577f05ff38c0454a529f8e25d70043166c3c843ba386b8533d1566010fb3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c37b5c0566194412a917f8b555c9713ff611891282349436c1825e2035304e0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__134b61ab92cc43448c72979bf06fe8c5b99e11026860e775bc799d1ac6f3485c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85fa037be9d97ba3c80cd93837e11c8dbd4fe3a9d81a3b57bc62c3008fc0d045(
    value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnForm.SectionalElementProperty, _IResolvable_da3f097b]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70860863c037915af307f857edb8d06dc079e810fc30f8a36441c45da0c1bed9(
    value: typing.Union[CfnForm.FormStyleProperty, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6086ddf273ace487109ec97dd1dc720c5f83ebbe24a96e2c42ae15646389d00(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcc01bb0df0b0a573caa23a9628b8cbfe2eb86510e0e390b92156dd05d486862(
    value: typing.Optional[typing.Union[CfnForm.FormCTAProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34caf84fc388835a97bc0ea839fd35da20c88a4c8e915204f78e924b66d4de02(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__facb12c1ebfafe4ee51a4282ac25081c6fb10fb0a82684aa169cb14fa6886efa(
    *,
    excluded: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    input_type: typing.Optional[typing.Union[typing.Union[CfnForm.FieldInputConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    label: typing.Optional[builtins.str] = None,
    position: typing.Optional[typing.Union[typing.Union[CfnForm.FieldPositionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    validations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnForm.FieldValidationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2888e21dd850d2c3de4d4315337f2f5230a52e49287aa72328d2ad14617f64fa(
    *,
    type: builtins.str,
    default_checked: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    default_country_code: typing.Optional[builtins.str] = None,
    default_value: typing.Optional[builtins.str] = None,
    descriptive_text: typing.Optional[builtins.str] = None,
    max_value: typing.Optional[jsii.Number] = None,
    min_value: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    placeholder: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    step: typing.Optional[jsii.Number] = None,
    value: typing.Optional[builtins.str] = None,
    value_mappings: typing.Optional[typing.Union[typing.Union[CfnForm.ValueMappingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04a52fac39933b10d1cbbd03b00473e170b2984c315c7a3da3846dcc962e71c9(
    *,
    below: typing.Optional[builtins.str] = None,
    fixed: typing.Optional[builtins.str] = None,
    right_of: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34136205c95f2f635b9e01e36902998c37a6de39668801b785b9506c14054296(
    *,
    type: builtins.str,
    num_values: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
    str_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    validation_message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aaebf617bf3553d285de51deaea2efd0785ae24ec5569ffb2d9a60d69da4425(
    *,
    children: typing.Optional[builtins.str] = None,
    excluded: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    position: typing.Optional[typing.Union[typing.Union[CfnForm.FieldPositionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77c752ecf91acd1ce1f6b4872c5597ec73be17115bab2a5f704d816a5af501d4(
    *,
    cancel: typing.Optional[typing.Union[typing.Union[CfnForm.FormButtonProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    clear: typing.Optional[typing.Union[typing.Union[CfnForm.FormButtonProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    position: typing.Optional[builtins.str] = None,
    submit: typing.Optional[typing.Union[typing.Union[CfnForm.FormButtonProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c13c26fc166a4f957568be30eae909c624b75f8f8139e0588fece7eeee3282ae(
    *,
    data_source_type: builtins.str,
    data_type_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18fb1cc6c981a6a2bd1a5b53248a9d11f4a7c98e09a7132c1a7ca82bcd56c726(
    *,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eee01779eb429842d3c379bc94ce33ffc0e13bb071fc183cfbefbf30d80f6b8(
    *,
    token_reference: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50be8c564fec3c46684431a761d27d986411251dd2dbff52def67a46d2b37f76(
    *,
    horizontal_gap: typing.Optional[typing.Union[typing.Union[CfnForm.FormStyleConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    outer_padding: typing.Optional[typing.Union[typing.Union[CfnForm.FormStyleConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    vertical_gap: typing.Optional[typing.Union[typing.Union[CfnForm.FormStyleConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6d8665fe6651d5620544536ddb9794f1f75f8f980fd73240f5d8c373dec173(
    *,
    type: builtins.str,
    level: typing.Optional[jsii.Number] = None,
    orientation: typing.Optional[builtins.str] = None,
    position: typing.Optional[typing.Union[typing.Union[CfnForm.FieldPositionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a419a9779cbf833c1ce04bf2e120ab8acfe6226e2a461b0e4f2dce065c4c1b(
    *,
    value: typing.Union[typing.Union[CfnForm.FormInputValuePropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    display_value: typing.Optional[typing.Union[typing.Union[CfnForm.FormInputValuePropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d724ce98e4e33046526453a6db65965e6f336a8f4ff6e0f67b70823d84267d95(
    *,
    values: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnForm.ValueMappingProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bb63d5cc6b32485abf45108b28446e1c750de14c1855dae86134a9765f5dbf4(
    *,
    data_type: typing.Union[typing.Union[CfnForm.FormDataTypeConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    fields: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnForm.FieldConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    form_action_type: builtins.str,
    name: builtins.str,
    schema_version: builtins.str,
    sectional_elements: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnForm.SectionalElementProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    style: typing.Union[typing.Union[CfnForm.FormStyleProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    app_id: typing.Optional[builtins.str] = None,
    cta: typing.Optional[typing.Union[typing.Union[CfnForm.FormCTAProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    environment_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2279f682c519f8cd82b48b2513abcff891e39a55368285f7ff433a9378321040(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    values: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnTheme.ThemeValuesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnTheme.ThemeValuesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab465f089075b33a373e16d0ddf12b8c4ce3438c656f46db2c8ac0ac15208a34(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a229aebaa77e6195b91d905366ce47f16aebf09185cd76886e729ba2b05c685(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37420262c86d20249895865fc6efbd1cf14792658f7f10af8ab3410f125160d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb8701acac3d1216eee5ea6afa5963493d323823cf518c1ba70eebb677f169f7(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTheme.ThemeValuesProperty, _IResolvable_da3f097b]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__447d8cae12df687b1981d85cd7ad953ecb265c415202fa332bdb6ac0bdbc8d7f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnTheme.ThemeValuesProperty, _IResolvable_da3f097b]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__968a2203f12b6fe147c86388655984948ce554ab590d84eab56303a5cb4f1443(
    *,
    children: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnTheme.ThemeValuesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32916eb6e9dca0f7a126b89c19d4efd2943a6c491612af96a25d95ebbc0772d4(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[typing.Union[typing.Union[CfnTheme.ThemeValueProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77360f99c7978648939d69b66977b92aefcb6819d200949e380c72c121fb7bad(
    *,
    name: builtins.str,
    values: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnTheme.ThemeValuesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]],
    overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnTheme.ThemeValuesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

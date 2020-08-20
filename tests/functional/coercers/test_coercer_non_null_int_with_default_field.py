import pytest


@pytest.mark.asyncio
@pytest.mark.with_schema_stack(preset="coercion")
@pytest.mark.parametrize(
    "query,variables,expected",
    [
        (
            """query { nonNullIntWithDefaultField }""",
            None,
            {"data": {"nonNullIntWithDefaultField": "SUCCESS-123459"}},
        ),
        (
            """query { nonNullIntWithDefaultField(param: null) }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 1, "column": 43}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    }
                ],
            },
        ),
        (
            """query { nonNullIntWithDefaultField(param: 10) }""",
            None,
            {"data": {"nonNullIntWithDefaultField": "SUCCESS-13"}},
        ),
        (
            """query ($param: Int) { nonNullIntWithDefaultField(param: $param) }""",
            None,
            {"data": {"nonNullIntWithDefaultField": "SUCCESS-123459"}},
        ),
        (
            """query ($param: Int) { nonNullIntWithDefaultField(param: $param) }""",
            {"param": None},
            {
                "data": {"nonNullIntWithDefaultField": None},
                "errors": [
                    {
                        "message": "Argument < param > of non-null type < Int! > must not be null.",
                        "path": ["nonNullIntWithDefaultField"],
                        "locations": [{"line": 1, "column": 57}],
                    }
                ],
            },
        ),
        (
            """query ($param: Int) { nonNullIntWithDefaultField(param: $param) }""",
            {"param": 20},
            {"data": {"nonNullIntWithDefaultField": "SUCCESS-23"}},
        ),
        (
            """query ($param: Int = null) { nonNullIntWithDefaultField(param: $param) }""",
            None,
            {
                "data": {"nonNullIntWithDefaultField": None},
                "errors": [
                    {
                        "message": "Argument < param > of non-null type < Int! > must not be null.",
                        "path": ["nonNullIntWithDefaultField"],
                        "locations": [{"line": 1, "column": 64}],
                    }
                ],
            },
        ),
        (
            """query ($param: Int = null) { nonNullIntWithDefaultField(param: $param) }""",
            {"param": None},
            {
                "data": {"nonNullIntWithDefaultField": None},
                "errors": [
                    {
                        "message": "Argument < param > of non-null type < Int! > must not be null.",
                        "path": ["nonNullIntWithDefaultField"],
                        "locations": [{"line": 1, "column": 64}],
                    }
                ],
            },
        ),
        (
            """query ($param: Int = null) { nonNullIntWithDefaultField(param: $param) }""",
            {"param": 20},
            {"data": {"nonNullIntWithDefaultField": "SUCCESS-23"}},
        ),
        (
            """query ($param: Int = 30) { nonNullIntWithDefaultField(param: $param) }""",
            None,
            {"data": {"nonNullIntWithDefaultField": "SUCCESS-33"}},
        ),
        (
            """query ($param: Int = 30) { nonNullIntWithDefaultField(param: $param) }""",
            {"param": None},
            {
                "data": {"nonNullIntWithDefaultField": None},
                "errors": [
                    {
                        "message": "Argument < param > of non-null type < Int! > must not be null.",
                        "path": ["nonNullIntWithDefaultField"],
                        "locations": [{"line": 1, "column": 62}],
                    }
                ],
            },
        ),
        (
            """query ($param: Int = 30) { nonNullIntWithDefaultField(param: $param) }""",
            {"param": 20},
            {"data": {"nonNullIntWithDefaultField": "SUCCESS-23"}},
        ),
        (
            """query ($param: Int!) { nonNullIntWithDefaultField(param: $param) }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    }
                ],
            },
        ),
        (
            """query ($param: Int!) { nonNullIntWithDefaultField(param: $param) }""",
            {"param": None},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > of non-null type < Int! > must not be null.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    }
                ],
            },
        ),
        (
            """query ($param: Int!) { nonNullIntWithDefaultField(param: $param) }""",
            {"param": 20},
            {"data": {"nonNullIntWithDefaultField": "SUCCESS-23"}},
        ),
    ],
)
async def test_coercion_non_null_int_with_default_field(
    schema_stack, query, variables, expected
):
    assert await schema_stack.execute(query, variables=variables) == expected

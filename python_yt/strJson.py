from typing import Any
import json

def patch_server_details(
        server_id: str,
        oneview: str | None = None,
        **kwargs: Any,
    ):
        body = {}
        if oneview is not None:
            body["oneview"] = oneview

        data=json.dumps(body)
        print(data)

patch_server_details(
        "1234",
        oneview={
                "applianceUri": "APPLIANCE_URI"
        },
    )

oneviews={
                "applianceUri": "APPLIANCE_URI"
        },

print(type(oneviews))


"""
ShopEasy Customer Lookup Lambda
================================
Episode 3 of the ShopEasy Amazon Connect series.

Invoked by an Amazon Connect contact flow during the welcome step.
Takes the caller's phone number, looks up the customer in DynamoDB,
and returns their profile data as contact attributes.

Expected event payload from Connect:
    event["Details"]["ContactData"]["CustomerEndpoint"]["Address"] = "+15551234567"

Returns a flat dict of strings (Connect requires string values for attributes):
    {
        "customer_found": "true",
        "first_name": "Sarah",
        "loyalty_tier": "gold",
        "last_order_status": "delivered",
        "last_order_number": "ORD-1042"
    }

If the customer isn't found, returns customer_found = "false" so the
flow can branch accordingly. Never raises — Connect handles errors badly,
so we always return a usable dict.
"""

import os
import boto3
from botocore.exceptions import ClientError


# Table name comes from an environment variable so we don't hardcode it.
# Set CUSTOMERS_TABLE_NAME = "shopeasy-customers" on the Lambda configuration.
TABLE_NAME = os.environ.get("CUSTOMERS_TABLE_NAME", "shopeasy-customers")

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    """Entry point invoked by Amazon Connect."""

    phone_number = _extract_phone_number(event)
    print(f"Looking up customer with phone: {phone_number}")

    if not phone_number:
        return _not_found_response("missing_phone_number")

    try:
        response = table.get_item(Key={"phone_number": phone_number})
    except ClientError as e:
        print(f"DynamoDB error: {e}")
        return _not_found_response("lookup_error")

    item = response.get("Item")
    if not item:
        print(f"No customer found for {phone_number}")
        return _not_found_response("not_in_database")

    # Build the response — every value must be a string for Connect.
    return {
        "customer_found": "true",
        "first_name": str(item.get("first_name", "")),
        "last_name": str(item.get("last_name", "")),
        "email": str(item.get("email", "")),
        "loyalty_tier": str(item.get("loyalty_tier", "standard")),
        "last_order_number": str(item.get("last_order_number", "")),
        "last_order_status": str(item.get("last_order_status", "")),
    }


def _extract_phone_number(event):
    """Pull the caller's phone number out of the Connect event payload."""
    try:
        return event["Details"]["ContactData"]["CustomerEndpoint"]["Address"]
    except (KeyError, TypeError):
        return None


def _not_found_response(reason):
    """Return a default response when no customer is found.

    The flow checks customer_found to decide whether to personalize the
    greeting or use the generic version.
    """
    return {
        "customer_found": "false",
        "first_name": "",
        "last_name": "",
        "email": "",
        "loyalty_tier": "standard",
        "last_order_number": "",
        "last_order_status": "",
        "lookup_failure_reason": reason,
    }

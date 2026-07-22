#!/usr/bin/env python3
"""
PLS v0.1 Validation Tool
Author: AI MacRae
"""

import json
import jsonschema
import sys

def validate_ledger(ledger_file, schema_file):
    with open(schema_file, 'r') as f:
        schema = json.load(f)
    with open(ledger_file, 'r') as f:
        ledger = json.load(f)
    
    try:
        jsonschema.validate(ledger, schema)
        print(f"✅ {ledger_file} is VALID")
        return True
    except jsonschema.ValidationError as e:
        print(f"❌ {ledger_file} is INVALID: {e.message}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 validation-tool.py <ledger-file.json> <schema-file.json>")
        sys.exit(1)
    
    sys.exit(0 if validate_ledger(sys.argv[1], sys.argv[2]) else 1)
import os
import jadn
import json
import jsonschema

cdir = os.path.dirname(os.path.realpath('__file__'))  # Current directory
idata = os.path.join(cdir, 'data', 'reporting-example1.json')
ischema = os.path.join(cdir, 'schema', 'reporting-v1.0.jadn')

# Validate example serialization with JADN schema
schema = jadn.load(ischema)
codec = jadn.codec.Codec(schema, verbose_rec=True, verbose_str=True)
with open(idata) as fp:
    example = json.load(fp)
example_json = codec.encode('Monitoring-Overlay', example)

# Translate JADN schema to JSON Schema format
jschema = json.loads(jadn.translate.json_schema_dumps(schema))

# Validate example serialization with JSON Schema
jsonschema.Draft7Validator(jschema).validate(example)
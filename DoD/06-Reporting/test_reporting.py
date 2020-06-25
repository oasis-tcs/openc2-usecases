import os
import jadn
import json
import jsonschema

cdir = os.path.dirname(os.path.realpath('__file__'))  # Current directory
data_file = os.path.join(cdir, 'data', 'reporting-example1.json')
schema_file = os.path.join(cdir, 'schema', 'reporting-v1.0.jadn')
with open(data_file) as fp:
    example = json.load(fp)

# Validate example with JADN schema
schema = jadn.load(schema_file)
codec = jadn.codec.Codec(schema, verbose_rec=True, verbose_str=True)
example_json = codec.encode('Monitoring-Overlay', example)

# Translate JADN schema to JSON Schema
jschema = json.loads(jadn.translate.json_schema_dumps(schema))

# Validate example with JSON Schema
jsonschema.Draft7Validator(jschema).validate(example)
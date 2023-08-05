# DRB Metadata Extractor
It's an applicative part using DRB allowing to extract metadata from
data according its topic.

## Metadata
### How to extract metadata ?
```python
from drb.metadata import DrbMetadataResolver
import drb.topics.resolver as resolver


if __name__ == '__main__':
    node = resolver.create('<my_resource_url>')
    metadata = DrbMetadataResolver().get_metadata(node)
    for md_name, md in metadata.items():
        print(md_name, ' -- ', md.extract(node))

```

### How to define metadata ?
Metadata are defined in a `cortex.yaml` file following the template:
```yaml
drbItemClass: <topic_uuid>           # target topic
variables:                           # variable list
  - name: <var_name>                   # variable name
    <extractor>: <extractor_content>   # an extractor
metadata:                            # metadata list
  - name: my_metadata                  # metadata name
    <extractor>: <extractor_content>   # an extractor
```

- metadata are applied to their target topic and its derivatives
- inherited metadata is override if it's redefined in a derivative topic
- variables are not transitive between a topic and its derivatives

### Extractor
An extractor as its name suggests allowing to extract information/data from
a node. An extractor is defined by a YAML content. Three extractor types exists
currently:

#### Constant
This extractor nothing from the node but give always the same value.

````yaml
constant: 42
````
Some string values are automatically converted to a specific Python type:

| Value                      | Python type       |
|----------------------------|-------------------|
| 2022-01-01                 | datatime.date     |
| 2022-01-01T00:00:00.000Z   | datatime.datetime |

#### XQuery
This extractor allowing to extract data from the node via an XQuery script.
See more details about [XQuery](https://www.w3.org/TR/xquery-31/).

```yaml
xquery: |
  data(./manifest.safe/XFDU/metadataSection/
  metadataObject[@ID="generalProductInformation"]/metadataWrap/xmlData/
    *[matches(name(),"standAloneProductInformation|generalProductInformation")]/
    noiseCompressionType)
```

#### Python
The Python extractor allowing to extract data from a node via a Python script.
Where the `node` variable represents the current node.

```yaml
python: |
  return node['DATASTRIP'][0]['MTD_DS.xml']['Level-1C_DataStrip_ID']
      ['General_Info']['Datatake_Info'].get_attribute('datatakeIdentifier')
```


example:
```yaml
drbItemClass: aff2191f-5b06-4121-a9fa-f3d93f6c6331
variables:
  - name: node_platform
    xquery: |
      ./manifest.safe/XFDU/metadataSection/metadataObject[@ID="platform"]/
        metadataWrap/xmlData/platform
metadata:
  - name: 'platformName'
    constant: 'Sentinel-1'
  - name: 'SatelliteNumber'
    xquery: |
      declare variable $node_platform external;
      data($node_platform/number)
  - name: 'platformIdentifier'
    python: |
      return node_platform['nssdcIdentifier'].value
  - name: 'resolutionDetail'
    python: |
      resolution = node.name[10:11]
      if resolution == 'F':
        return 'Full'
      elif resolution == 'H':
        return 'High'
      elif resolution == 'M':
        return 'Medium'
      return None
```

### Packaging
The package python containing metadata of a DRB topic must have the following
instruction:
 - a `drb.metadata` entry point whose its value is the targeted Python
   package containing the `cortex.yaml` file

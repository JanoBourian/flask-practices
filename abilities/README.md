# Github Repository

https://github.com/eazybytes/yaml

# Conversor 

https://www.json2yaml.com/convert-yaml-to-json 


# Best conversor

https://yaml-online-parser.appspot.com/

# Better?

https://onlineyamltools.com/convert-yaml-to-json

# YAML viewer

https://jsonformatter.org/yaml-viewer

# Install yamllint

```
pip install yamllint
yamllint .
```

Is posible design our personal configurations. Check documentation for yamllint

## Types suport 

-> !!str 

- Scalar
- Collections
- Styles 
- Block Style
- Flow Style

## First types 

- Scalar types: 
    - Integer (int)
    - Float (float)
    - String (str)
    - Boolean (bool)
    - Date and DateTime (timestamp)
    - Images (binary)
- Collections types:
    - Sequence (seq)
    - Map (map)
    - Ordered Map (omap)
    - Pairs (pairs)
    - Set (set)
- Styles:
    - Block style
    - Flow style

## YAML FEATURES

- Anchors:
    - Duplicate Content
    - Represent Complex Type
    - Inherit Properties
    - Deep Dive: Anchors and Merge Keys
    - Documents in YAML

- Usages: 
    - &curCourse, the new asigments have *
    - course how array
    - inherit with anchors <<: *course5001

## YAML DIRECTIVES
- YAML Directives 
    - %DIRECTIVE params 
    - %YAML version
- Tag Directive 
    - %TAG shortcut for URI prefixes 
    - %TAG handle prefix
- Tag Handles
    - !
    - !!
    - !name!
- Tag Prefixes

Data Product Definitions must conform to the following set of rules:

## Definition specification format

Each definition must be described in corresponding JSON file, which is an OpenAPI 3.x
spec. Name of this file must be in UpperCamelCase.

## OpenAPI schema

_Rules below are applied for each definition._

### Spec file must define only one POST endpoint

> ❌ Wrong: Two endpoints defined

```json
{
  "paths": {
    "/AirQuality/Current": { "post": {} },
    "/Company/BasicInfo": {}
  }
}
```

> ❌ Wrong: Endpoint has POST and GET method

```json
{
  "paths": {
    "/AirQuality/Current": { "post": {}, "get": {} }
  }
}
```

> ✅ Correct

```json
{
  "paths": {
    "/AirQuality/Current": { "post": {} }
  }
}
```

### Spec file must include title, description and summary fields

Main file must have a `title` and `description` and POST definition must contain
`summary` and `description` fields.

> ✅ Correct

```json
{
  "info": {
    "title": "Current air quality",
    "description": "Current air quality (AQI) in a given location"
  },
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "summary": "Current air quality",
        "description": "Current air quality (AQI) in a given location"
      }
    }
  }
}
```

### Spec file must include request body schema

> ✅ Correct

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CurrentAirQualityRequest"
              }
            }
          },
          "required": true
        },
        "components": {
          "schemas": {
            "CurrentAirQualityRequest": {}
          }
        }
      }
    }
  }
}
```

### Spec file must include schema for successful (200 OK) response

> ❌ Wrong: Responses section is empty

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "responses": {}
      }
    }
  }
}
```

> ❌ Wrong: CurrentAirQualityResponse reference is missing

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CurrentAirQualityResponse"
                }
              }
            }
          }
        }
      },
      "components": {
        "schemas": {
          "CompanyBasicInfoRequest": {}
        }
      }
    }
  }
}
```

> ✅ Correct

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CurrentAirQualityResponse"
                }
              }
            }
          }
        }
      },
      "components": {
        "schemas": {
          "CurrentAirQualityResponse": {}
        }
      }
    }
  }
}
```

### Schemas for request body and responses must be of `application/json` content type

> ❌ Wrong: Schema is by mistake defined for `multipart/form-data` content type

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/CurrentAirQualityRequest"
              }
            }
          },
          "required": true
        }
      }
    }
  }
}
```

> ✅ Correct

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CurrentAirQualityRequest"
              }
            }
          },
          "required": true
        }
      }
    }
  }
}
```

### Spec file must not define any severs

> ❌ Wrong: Server URLs provided

```json
{
  "servers": [{ "url": "https://example.com" }]
}
```

### Spec file must not define security section for API endpoint

> ❌ Wrong: Security section is defined for path

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "security": {
          "ApiKeyAuth": []
        }
      }
    }
  }
}
```

### All information should be described in American English

> ❌ Wrong: Definition name is in Finnish

```json
{
  "paths": {
    "/Grafiikka/Väri": { "post": {} }
  }
}
```

> ❌ Wrong: Definition name is in British English

```json
{
  "paths": {
    "/Graphics/Colour": { "post": {} }
  }
}
```

> ✅ Correct: Definition name is in American English

```json
{
  "paths": {
    "/Graphics/Color": { "post": {} }
  }
}
```

_Note: Same rule applies to all description fields._

### Spec file should list all the mandatory error responses

The following responses are required and must be defined:

- 401, 403, 404, 422, 444, 500, 502, 503, 504, 550

An
[example of a spec with all the error codes](https://github.com/ioxio-dataspace/ioxio-data-product-definition-tooling/blob/main/definition_tooling/converter/tests/__snapshots__/test_converter/test_air_quality.json)
can be found in the
[definition tooling repo](https://github.com/ioxio-dataspace/ioxio-data-product-definition-tooling/).

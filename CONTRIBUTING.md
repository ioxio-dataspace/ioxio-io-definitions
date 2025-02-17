# Contributing to Data Product Definitions

A big welcome and thank you for considering contributing to this project!

Reading and following these guidelines will help us make the contribution process easy
and effective for everyone involved. It also communicates that you agree to respect the
time of the developers managing and developing these open source projects. In return, we
will reciprocate that respect by addressing your issue, assessing changes, and helping
you finalize your pull requests.

## Quicklinks

- [Contributing to Data Product Definitions](#contributing-to-data-product-definitions)
  - [Quicklinks](#quicklinks)
  - [Getting Started](#getting-started)
  - [Definitions format](#definitions-format)
  - [Adding new Data Product Definition](#adding-new-data-product-definition)
    - [Raw OpenApi spec](#raw-openapi-spec)
    - [Definition as a Python file](#definition-as-a-python-file)
  - [Pull Requests](#pull-requests)
  - [License](#license)

## Getting Started

New definitions should be submitted as a pull request to this repository. We try our
best to provide an automated validation of the most common mistakes in the definitions
format, but it's still better to go through the definition guidelines.

## Definitions format

The most complete set of rules with examples can be found in the
[DataProducts](./DataProducts/README.md) directory. Except of that, please make sure to
meet the following criterias:

1. Use American English for describing data
2. Each definition file must define only one POST endpoint
3. Each definition file must include a schema for a successful response
4. Each definition file must include a schema for the request body
5. Each definition file must not define any severs or security sections

## Adding new Data Product Definition

### Definition as a Python file

Definitions are created using Python and a set of
[pydantic](https://github.com/pydantic/pydantic) models. The converter from the
[ioxio-data-product-definition-tooling](https://github.com/ioxio-dataspace/ioxio-data-product-definition-tooling)
takes care of converting each `.py` file to the corresponding `.json` OpenAPI spec file.

For example, to add a definition for `Foo/Bar` version `0.1.0`:

- create `src/Foo/Bar_v0.1.py`

You have 2 options to use the converter:

1. By running `pre-commit install` after cloning the repo. Then definitions will be
   converted automatically before each commit (recommended).
2. By creating a PR to the `main` branch. CI workflow will run the automation and push
   updated/generated files if needed.

### Versioning of definitions

Definitions have version numbers that are `>= 0.1.0` and they should follow
[Semantic Versioning](https://semver.org/) of the form `MAJOR.MINOR.PATCH`.

A general rule of thumb would be that the first definition should be versioned as
`0.1.0`. Any backward-compatible changes to it should increment the PATCH number (i.e.
`z` in `0.y.z`) and any breaking changes increment the MINOR number (i.e. increment `y`
in `0.y.z` and reset `z` to `0`).

Once the definition has been tested out a bit in practice and can be considered stable a
`1.0.0` version should be created. As per normal Semantic Versioning rules, any trivial
changes that does not break anything (for example fixing a typo in a description that
does not affect the data being transferred) should update the PATCH version, any new
backwards compatible functionality (like adding a new optional field) should update the
MINOR version and any breaking changes (like renaming a field or adding a new required
field) should increment the MAJOR version number (i.e. `1.2.3` -> `2.0.0`).

The version number in the definitions are reflected in the filenames and the URL path to
the data product. In the filename and URL the version is added to the end and separated
by `_v`, followed by the `MAJOR.MINOR` part of the version number. The `.PATCH` part is
left out as those changes are not allowed to change anything in the actual data format.
Any possible pre-release identifiers are included though. For example version `1.2.3` of
the `Foo/Bar` definition would correspond to the file `src/Foo/Bar_v1.2.py` and will be
requested from a URL of the form `/Foo/Bar_v1.2`.

Note that each time the MINOR version is updated the file is changed in place and when
the MAJOR or MINOR version number is updated a new definition file is created. At the
same time the definitions in the previous files are usually marked as deprecated. The
deprecation rules and deletion of old definitions can vary per dataspace.

Example of a typical flow of versions and corresponding filenames:

- `0.1.0` -> `src/Foo/Bar_v0.1.py` The first version.
- `0.1.1` -> `src/Foo/Bar_v0.1.py` Fix a typo in a title or description.
- `0.2.0` -> `src/Foo/Bar_v0.2.py` Add an optional or required field or rename a field.
- `0.2.1` -> `src/Foo/Bar_v0.2.py` Fix a typo in a title or description.
- `1.0.0` -> `src/Foo/Bar_v1.0.py` First stable release.
- `1.0.1` -> `src/Foo/Bar_v1.0.py` Fix a typo in a title or description.
- `1.1.0` -> `src/Foo/Bar_v1.1.py` Add a new optional field.
- `2.0.0` -> `src/Foo/Bar_v2.0.py` Rename a field or add a new required field.
- `3.0.0-beta` -> `src/Foo/Bar_v3.0-beta.py` Major rewrite of the whole definition
  structure that needs to be tested before being considered ready to be used.
- `3.0.0-beta.2` -> `src/Foo/Bar_v3.0-beta.2.py` Changes to data being transferred.
- `3.0.0` -> `src/Foo/Bar_v3.0.py` Final new version of the definition.

## Pull Requests

In general, we follow the ["fork-and-pull" Git workflow](https://github.com/susam/gitpr)

1. Fork the repository to your own Github account
2. Clone the project to your machine
3. Create a branch locally with a succinct but descriptive name
4. Commit changes to the branch
5. Following any formatting and testing guidelines specific to this repo Push changes to
   your fork
6. Open a PR in our repository

## License

By contributing, you agree that your contributions will be licensed under its
[MIT License](./LICENSE).

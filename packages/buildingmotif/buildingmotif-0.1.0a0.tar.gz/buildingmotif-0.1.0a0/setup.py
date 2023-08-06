# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['buildingmotif',
 'buildingmotif.api',
 'buildingmotif.api.serializers',
 'buildingmotif.api.views',
 'buildingmotif.building_motif',
 'buildingmotif.database',
 'buildingmotif.dataclasses',
 'buildingmotif.ingresses',
 'buildingmotif.libraries']

package_data = \
{'': ['*'],
 'buildingmotif': ['resources/*'],
 'buildingmotif.libraries': ['brick/*', 'constraints/*']}

install_requires = \
['Flask-API>=3.0.post1,<4.0',
 'Flask>=2.1.2,<3.0.0',
 'SQLAlchemy>=1.4,<2.0',
 'alembic>=1.8.0,<2.0.0',
 'nbmake>=1.3.0,<2.0.0',
 'networkx>=2.7.1,<3.0.0',
 'pyaml>=21.10.1,<22.0.0',
 'pyshacl>=0.19.1,<0.20.0',
 'rdflib-sqlalchemy>=0.5.3,<0.6.0',
 'rdflib==6.1.1',
 'rfc3987>=1.3.8,<2.0.0',
 'setuptools>=65.6.3,<66.0.0',
 'types-PyYAML>=6.0.4,<7.0.0']

extras_require = \
{':extra == "bacnet-ingress" or extra == "all-ingresses"': ['BAC0>=22.9.21,<23.0.0',
                                                            'netifaces>=0.11.0,<0.12.0'],
 ':extra == "xlsx-ingress" or extra == "all-ingresses"': ['openpyxl>=3.0.10,<4.0.0']}

setup_kwargs = {
    'name': 'buildingmotif',
    'version': '0.1.0a0',
    'description': 'Building Metadata OnTology Interoperability Framework',
    'long_description': '# BuildingMOTIF\n\n[![codecov](https://codecov.io/gh/NREL/BuildingMOTIF/branch/main/graph/badge.svg?token=HAFSYH45NX)](https://codecov.io/gh/NREL/BuildingMOTIF) \n[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://nrel.github.io/BuildingMOTIF/)\n![PyPI](https://img.shields.io/pypi/v/buildingmotif)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/buildingmotif)\n\n> *Enabling the enabling technology of semantic interoperability.*\n\nSemantic Interoperability in buildings through standardized semantic metadata is crucial in unlocking the value of the abundant and diverse networked data in buildings, avoiding subsequent data incompatibility/interoperability issues, and paving the way for advanced building technologies like Fault Detection and Diagnostics (FDD), real-time energy optimization, other energy management information systems ([EMIS](https://www.energy.gov/eere/femp/what-are-energy-management-information-systems)), improved HVAC controls, and grid-integrated energy efficient building ([GEB](https://www.energy.gov/eere/buildings/grid-interactive-efficient-buildings)) technologies, all of which are needed to fully de-carbonize buildings.\n\nUtilizing the capabilities of [Semantic Web](https://www.w3.org/standards/semanticweb/), it is possible to standardize building metadata in structured, expressive, and machine-readable way, but at the same time it is very important to make it easier to implement for field practitioners without advanced knowledge in computer science. ***Building Metadata OnTology Interoperability Framework (BuildingMOTIF)*** bridges that gap between theory and practice, by offering a toolset for building metadata creation, storage, visualization, and validation. It is offered in the form of a SDK with easy-to-use APIs, which abstract the underlying complexities of [RDF](https://www.w3.org/RDF/) graphs, database management, [SHACL](https://www.w3.org/TR/shacl/) validation, and interoperability between different metadata schemas/ontologies. It also supports connectors for easier integration with existing metadata sources (e.g., Building Automation System data, design models, existing metadata models, etc.) which are available at different phases of the building life-cycle.\n\nThe objectives of the ***BuildingMOTIF*** toolset are to (1) lower costs, reduce installation time, and improve delivered quality of building controls and services for building owners and occupants, (2) enable a simpler and more easily verifiable procurement process for products and services for building managers, and (3) open new business opportunities for service providers, by removing knowledge barriers for parties implementing building controls and services.\n\nCurrently, ***BuildingMOTIF*** is planned to support [Brick](https://brickschema.org/) Schema, [Project Haystack](https://project-haystack.org/), and the upcoming [ASHRAE 223P](https://www.ashrae.org/about/news/2018/ashrae-s-bacnet-committee-project-haystack-and-brick-schema-collaborating-to-provide-unified-data-semantic-modeling-solution) standard, and to offer both UI and underlying SDK with tutorials and reference documentation to be useful for different levels of expertise of users for maximum adoption.\n\n# Documentation\n\nThe documentation uses Diataxis[^1] as a framework for its structure, which is organized into the following sections.\n\n[^1]: https://diataxis.fr/\n\n## Reference\n\n- [Developer Documentation](https://nrel.github.io/BuildingMOTIF/reference/developer_documentation.html)\n- [Code Documentation](https://nrel.github.io/BuildingMOTIF/reference/apidoc/index.html)\n\n## Tutorials\n\n- [Model Creation](https://nrel.github.io/BuildingMOTIF/tutorials/model_creation.html)\n- [Model Validation](https://nrel.github.io/BuildingMOTIF/tutorials/model_validation.html)\n- [Model Correction](https://nrel.github.io/BuildingMOTIF/tutorials/model_correction.html)\n- [Template Writing](https://nrel.github.io/BuildingMOTIF/tutorials/template_writing.html)\n\n## Guides\n\n🏗️ under construction\n\n## Explanation\n\n🏗️ under construction\n',
    'author': 'Hannah Eslinger',
    'author_email': 'Hannah.Eslinger@nrel.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NREL/BuildingMOTIF',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

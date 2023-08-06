# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ontogpt',
 'ontogpt.clients',
 'ontogpt.converters',
 'ontogpt.engines',
 'ontogpt.evaluation',
 'ontogpt.evaluation.ctd',
 'ontogpt.evaluation.drugmechdb',
 'ontogpt.evaluation.drugmechdb.datamodel',
 'ontogpt.evaluation.go',
 'ontogpt.evaluation.hpoa',
 'ontogpt.io',
 'ontogpt.templates',
 'ontogpt.webapp']

package_data = \
{'': ['*'],
 'ontogpt.evaluation.ctd': ['database/*'],
 'ontogpt.webapp': ['html/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'airium>=0.2.5,<0.3.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'bioc>=2.0.post5,<3.0',
 'class-resolver>=0.3.10,<0.4.0',
 'click>=8.1.3,<9.0.0',
 'eutils>=0.6.0,<0.7.0',
 'fastapi>=0.88.0,<0.89.0',
 'gilda>=0.10.3,<0.11.0',
 'importlib>=1.0.4,<2.0.0',
 'inflect>=6.0.2,<7.0.0',
 'jsonlines>=3.1.0,<4.0.0',
 'linkml-owl>=0.2.4,<0.3.0',
 'linkml>=1.4.1,<2.0.0',
 'mkdocs-mermaid2-plugin>=0.6.0,<0.7.0',
 'oaklib>=0.1.64,<0.2.0',
 'openai>=0.25.0,<0.26.0',
 'python-multipart>=0.0.5,<0.0.6',
 'setuptools>=65.5.0,<66.0.0',
 'tiktoken>=0.1.1,<0.2.0',
 'tox>=3.25.1,<4.0.0',
 'uvicorn>=0.20.0,<0.21.0',
 'wikipedia>=1.4.0,<2.0.0']

extras_require = \
{':extra == "docs"': ['sphinx[docs]>=5.3.0,<6.0.0',
                      'sphinx-rtd-theme[docs]>=1.0.0,<2.0.0',
                      'sphinx-autodoc-typehints[docs]>=1.19.4,<2.0.0',
                      'sphinx-click[docs]>=4.3.0,<5.0.0',
                      'myst-parser[docs]>=0.18.1,<0.19.0']}

entry_points = \
{'console_scripts': ['ontogpt = ontogpt.cli:main',
                     'web-ontogpt = ontogpt.webapp.main:start']}

setup_kwargs = {
    'name': 'ontogpt',
    'version': '0.1.1',
    'description': 'OntoGPT',
    'long_description': "# OntoGPT\n\nGeneration of Ontologies and Knowledge Bases using GPT\n\nA knowledge extraction tool that uses a large language model to extract semantic information from text.\n\nThis exploits the ability of ultra-LLMs such as GPT-3 to return user-defined data structures\nas a response.\n\nCurrently there are two different pipelines implemented:\n\n- SPIRES: Structured Prompt Interrogation and Recursive Extraction of Semantics\n    - Zero-shot learning approach to extracting nested semantic structures from text\n    - Inputs: LinkML schema + text\n    - Outputs: JSON, YAML, or RDF or OWL that conforms to the schema\n    - Uses text-davinci-003\n- HALO: HAllucinating Latent Ontologies \n    - Few-shot learning approach to generating/hallucinating a domain ontology given a few examples\n    - Uses code-davinci-002\n\n## SPIRES: Usage\n\nGiven a short text `abstract.txt` with content such as:\n\n   > The cGAS/STING-mediated DNA-sensing signaling pathway is crucial\n   for interferon (IFN) production and host antiviral\n   responses\n   > \n   > ...\n   > [snip] \n   > ...\n   > \n   > The underlying mechanism was the\n   interaction of US3 with β-catenin and its hyperphosphorylation of\n   β-catenin at Thr556 to block its nuclear translocation\n   > ...\n   > ...\n\n(see [full input](tests/input/cases/gocam-betacat.txt))\n\nWe can extract this into the [GO pathway datamodel](src/ontogpt/templates/gocam.yaml):\n\n```bash\nontogpt extract -t gocam.GoCamAnnotations abstract.txt\n```\n\nGiving schema-compliant yaml such as:\n\n```yaml\ngenes:\n- HGNC:2514\n- HGNC:21367\n- HGNC:27962\n- US3\n- FPLX:Interferon\n- ISG\ngene_gene_interactions:\n- gene1: US3\n  gene2: HGNC:2514\ngene_localizations:\n- gene: HGNC:2514\n  location: Nuclear\ngene_functions:\n- gene: HGNC:2514\n  molecular_activity: Transcription\n- gene: HGNC:21367\n  molecular_activity: Production\n...\n```\n\nSee [full output](tests/output/gocam-betacat.yaml)\n\nnote in the above the grounding is very preliminary and can be improved. Ungrounded NamedEntities appear as text.\n\n## How it works\n\n1. You provide an arbitrary data model, describing the structure you want to extract text into\n    - this can be nested (but see limitations below)\n2. provide your preferred annotations for grounding NamedEntity fields\n3. ontogpt will:\n    - generate a prompt\n    - feed the prompt to a language model (currently OpenAI)\n    - parse the results into a dictionary structure\n    - ground the results using a preferred annotator\n\n## Pre-requisites\n\n- python 3.9+\n- an OpenAI account\n- a BioPortal account (optional, for grounding)\n\nYou will need to set both API keys using OAK (which is a dependency of this project)\n\n```\npoetry run runoak set-apikey openai <your openai api key>\npoetry run runoak set-apikey bioportal <your bioportal api key>\n```\n\n## How to define your own extraction data model\n\n### Step 1: Define a schema\n\nSee [src/ontogpt/templates/](src/ontogpt/templates/) for examples.\n\nDefine a schema (using a subset of LinkML) that describes the structure you want to extract from your text.\n\n```yaml\nclasses:\n  MendelianDisease:\n    attributes:\n      name:\n        description: the name of the disease\n        examples:\n          - value: peroxisome biogenesis disorder\n        identifier: true  ## needed for inlining\n      description:\n        description: a description of the disease\n        examples:\n          - value: >-\n             Peroxisome biogenesis disorders, Zellweger syndrome spectrum (PBD-ZSS) is a group of autosomal recessive disorders affecting the formation of functional peroxisomes, characterized by sensorineural hearing loss, pigmentary retinal degeneration, multiple organ dysfunction and psychomotor impairment\n      synonyms:\n        multivalued: true\n        examples:\n          - value: Zellweger syndrome spectrum\n          - value: PBD-ZSS\n      subclass_of:\n        multivalued: true\n        range: MendelianDisease\n        examples:\n          - value: lysosomal disease\n          - value: autosomal recessive disorder\n      symptoms:\n        range: Symptom\n        multivalued: true\n        examples:\n          - value: sensorineural hearing loss\n          - value: pigmentary retinal degeneration\n      inheritance:\n        range: Inheritance\n        examples:\n          - value: autosomal recessive\n      genes:\n        range: Gene\n        multivalued: true\n        examples:\n          - value: PEX1\n          - value: PEX2\n          - value: PEX3\n\n  Gene:\n    is_a: NamedThing\n    id_prefixes:\n      - HGNC\n    annotations:\n      annotators: gilda:, bioportal:hgnc-nr\n\n  Symptom:\n    is_a: NamedThing\n    id_prefixes:\n      - HP\n    annotations:\n      annotators: sqlite:obo:hp\n\n  Inheritance:\n    is_a: NamedThing\n    annotations:\n      annotators: sqlite:obo:hp\n```\n\n- the schema is defined in LinkML\n- prompt hints can be specified using the `prompt` annotation (otherwise description is used)\n- multivalued fields are supported\n- the default range is string - these are not grounded. E.g. disease name, synonyms\n- define a class for each NamedEntity\n- for any NamedEntity, you can specify a preferred annotator using the `annotators` annotation\n\nWe recommend following an established schema like biolink, but you can define your own.\n\n### Step 2: Compile the schema\n\nRun the `make` command at the top level. This will compile the schema to pedantic\n\n### Step 3: Run the command line\n\ne.g.\n\n```\nontogpt extract -t  mendelian_disease.MendelianDisease marfan-wikipedia.txt\n```\n\n## Web Application\n\nThere is a bare bones web application\n\n```\npoetry run web-ontogpt\n```\n\nNote that the agent running uvicorn must have the API key set, so for obvious reasons\ndon't host this publicly without authentication, unless you want your credits drained. \n\n## Features\n\n### Multiple Levels of nesting\n\nCurrently no more than two levels of nesting are recommended.\n\nIf a field has a range which is itself a class and not a primitive, it will attempt to nest\n\nE.g. the gocam schema has an attribute:\n\n```yaml\n  attributes:\n      ...\n      gene_functions:\n        description: semicolon-separated list of gene to molecular activity relationships\n        multivalued: true\n        range: GeneMolecularActivityRelationship\n```\n\nBecause GeneMolecularActivityRelationship is *inlined* it will nest\n\nThe generated prompt is:\n\n`gene_functions : <semicolon-separated list of gene to molecular activities relationships>`\n\nThe output of this is then passed through further SPIRES iterations.\n\n## Text length limit\n\nCurrently SPIRES must use text-davinci-003, which has a total 4k token limit (prompt + completion).\n\nYou can pass in a parameter to split the text into chunks, results will be recombined automatically,\nbut more experiments need to be done to determined how reliable this is.\n\n```\n\n## HALOE: Usage\n\nTODO\n\n## Limitations\n\n### Non-deterministic\n\nThis relies on an existing LLM, and LLMs can be fickle in their responses.\n\n### Coupled to OpenAI\n\nYou will need an openai account. In theory any LLM can be used but in practice the parser is tuned for OpenAI\n\n\n\n# Acknowledgements\n\nThis [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) project was developed from the [sphintoxetry-cookiecutter](https://github.com/hrshdhgd/sphintoxetry-cookiecutter) template and will be kept up-to-date using [cruft](https://cruft.github.io/cruft/).\n",
    'author': 'Chris Mungall',
    'author_email': 'cjmungall@lbl.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

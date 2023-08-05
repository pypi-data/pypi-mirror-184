# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torchmix',
 'torchmix.components',
 'torchmix.components.layers',
 'torchmix.core',
 'torchmix.nn',
 'torchmix.third_party']

package_data = \
{'': ['*']}

install_requires = \
['einops>=0.6.0,<0.7.0',
 'hydra-core>=1.3.1,<2.0.0',
 'hydra-zen>=0.8.0,<0.9.0',
 'jaxtyping>=0.2.11,<0.3.0']

setup_kwargs = {
    'name': 'torchmix',
    'version': '0.1.0rc2',
    'description': '',
    'long_description': '<h1 align="center">torchmix</h1>\n\n<h3 align="center">The missing component library for PyTorch</h3>\n\n<br />\n\nWelcome to torchmix, a collection of PyTorch modules that aims to reduce boilerplate and improve code modularity.\n\n**Please note: `torchmix` is currently in development and has not been tested for production use. The API may change at any time.**\n\n<br />\n\n## Usage\n\nTo use `torchmix`, simply import the desired components:\n\n```python\nimport torchmix.nn as nn  # Wrapped version of torch.nn\nfrom torchmix import (\n    Add,\n    Attach,\n    AvgPool,\n    ChannelMixer,\n    Extract,\n    PatchEmbed,\n    PositionEmbed,\n    PreNorm,\n    Repeat,\n    SelfAttention,\n    Token,\n)\n```\n\nYou can simply compose this components to build more complex architecture, as shown in the following example:\n\n```python\nvit_cls = nn.Sequential(\n    Add(\n        Attach(\n            PatchEmbed(dim=1024),\n            Token(dim=1024),\n        ),\n        PositionEmbed(\n            seq_length=196 + 1,\n            dim=1024,\n        ),\n    ),\n    Repeat(\n        nn.Sequential(\n            PreNorm(\n                ChannelMixer(\n                    dim=1024,\n                    expansion_factor=4,\n                    act_layer=nn.GELU.partial(),\n                ),\n                dim=1024,\n            ),\n            PreNorm(\n                SelfAttention(\n                    dim=1024,\n                    num_heads=8,\n                    head_dim=64,\n                ),\n                dim=1024,\n            ),\n        )\n    ),\n    Extract(0),\n)\n\nvit_avg = nn.Sequential(\n    Add(\n        PatchEmbed(dim=1024),\n        PositionEmbed(\n            seq_length=196,\n            dim=1024,\n        ),\n    ),\n    Repeat(\n        nn.Sequential(\n            PreNorm(\n                ChannelMixer(\n                    dim=1024,\n                    expansion_factor=4,\n                    act_layer=nn.GELU.partial(),\n                ),\n                dim=1024,\n            ),\n            PreNorm(\n                SelfAttention(\n                    dim=1024,\n                    num_heads=8,\n                    head_dim=64,\n                ),\n                dim=1024,\n            ),\n        )\n    ),\n    AvgPool(),\n)\n```\n\n### Integration with Hydra\n\nReproducibility is important, so it is always a good idea to store the configurations of your models. However, manually writing the configurations for complex, deeply nested PyTorch modules can be tedious and result in code that is difficult to understand and maintain. This is because the parent class may need to accept and pass along the parameters of its children classes, leading to a large number of arguments and strong coupling between the parent and child classes.\n\n`torchmix` simplifies this process by **auto-magically** generating the full configuration of a PyTorch module **simply by instantiating it.** This enables effortless integration with the `hydra` ecosystem, which allows for easy storage and management of module configurations.\n\nTo generate a configuration for a typical MLP using `torchmix`, for example, you can do the following:\n\n```python\nfrom torchmix import nn\n\nmodel = nn.Sequential(\n    nn.Linear(1024, 4096),\n    nn.Dropout(0.1),\n    nn.GELU(),\n    nn.Linear(4096, 1024),\n    nn.Dropout(0.1),\n)\n```\n\nYou can then store the configuration in the `hydra`\'s `ConfigStore` using:\n\n```python\nmodel.store(group="model", name="mlp")\n```\n\nAlternatively, you can export it to a YAML file if you want:\n\n```python\nmodel.export("mlp.yaml")\n```\n\nThis will generate the following configuration:\n\n```yaml\n_target_: torchmix.nn.Sequential\n_args_:\n  - _target_: torchmix.nn.Linear\n    in_features: 1024\n    out_features: 4096\n    bias: true\n    device: null\n    dtype: null\n  - _target_: torchmix.nn.Dropout\n    p: 0.1\n    inplace: false\n  - _target_: torchmix.nn.GELU\n    approximate: none\n  - _target_: torchmix.nn.Linear\n    in_features: 4096\n    out_features: 1024\n    bias: true\n    device: null\n    dtype: null\n  - _target_: torchmix.nn.Dropout\n    p: 0.1\n    inplace: false\n```\n\nYou can always instantiate the actual PyTorch module from its configuration using `hydra`\'s `instantiate` function.\n\nTo create custom modules with this functionality, simply subclass `MixModule` and define your module as you normally would:\n\n```python\nfrom torchmix import MixModule\n\nclass CustomModule(MixModule):\n    def __init__(self, num_heads, dim, depth):\n        pass\n\ncustom_module = CustomModule(16, 768, 12)\ncustom_module.store(group="model", name="custom")\n```\n\n## Documentation\n\nDocumentation is currently in progress. Please stay tuned! 🚀\n\n## Contributing\n\nWe welcome contributions to the `torchmix` library. If you have ideas for new components or suggestions for improving the library, don\'t hesitate to open an issue or start a discussion. Please note that `torchmix` is still in the prototype phase, so any contributions should be considered experimental.\n\n## License\n\n`torchmix` is licensed under the MIT License.\n',
    'author': 'junhsss',
    'author_email': 'junhsssr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

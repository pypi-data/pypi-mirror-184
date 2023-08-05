# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_servicestate', 'nonebot_plugin_servicestate.protocol']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.20,<0.24',
 'nonebot-adapter-onebot>=2.1.0,<3.0.0',
 'nonebot-plugin-localstore>=0.2.0,<0.3.0',
 'nonebot2>=2.0.0b2,<3.0.0',
 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-servicestate',
    'version': '0.1.2',
    'description': '基于NoneBot2的状态监测插件',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://user-images.githubusercontent.com/44545625/209862575-acdc9feb-3c76-471d-ad89-cc78927e5875.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n</p>\n\n<div align="center">\n\n# nonebot-plugin-servicestate\n\n_✨ NoneBot 服务状态查询插件 ✨_\n\n</div>\n\n<p align="center">\n  <a href="https://raw.githubusercontent.com/OREOCODEDEV/nonebot-plugin-servicestate/main/LICENSE">\n    <img src="https://img.shields.io/github/license/OREOCODEDEV/nonebot-plugin-servicestate.svg" alt="license">\n  </a>\n  <a href="https://pypi.org/project/nonebot-plugin-servicestate/">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-servicestate" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n</p>\n\n## 简介\n\n可通过 `服务状态` 查询当前服务器各功能 API 可用状态\n\n例如：\n\n```\nO 可用 | 会战面板\nO 可用 | 远程登录\nX 故障 | 涩图\nO 可用 | 画图\nX 故障 | ChatGPT\n```\n\n\n## 特色\n\n🚸 开箱即用：安装完成后无需修改任何配置项或代码即可使用\n\n💡 易于使用：所有配置项都可通过命令交互实现增删查改\n\n⚡️ 异步支持：所有协议均通过异步实现，无需担心探测过程中造成堵塞\n\n💻 开发友好：只需实现核心探测方法即可增添新协议支持，详情参考[添加协议](#添加协议)\n\n\n## 安装\n\n使用 `nb-cli` 安装（推荐）：\n```\nnb plugin install nonebot-plugin-servicestate\n```\n\n使用 `pip` 安装：\n```\npip install nonebot-plugin-servicestate\n```\n\n使用 `git clone` 安装：\n```\ngit clone https://github.com/OREOCODEDEV/nonebot-plugin-servicestate.git\n```\n\n\n## 使用\n\n### 服务状态查询\n可通过发送 `服务状态` 获取当前绑定的服务可用状态\n\n**只有服务状态查询无权限要求，服务的增删查改均需要 NoneBot 管理员权限，若服务增删查改命令不响应，请检查 NoneBot 是否已正确配置管理员**\n\n### 添加服务\n可通过发送 `添加服务 <协议> <名称> <地址>` 以添加需要监控的服务\n* 可在[此处](#协议支持)查看所有受支持的协议\n```\n添加服务 HTTP git截图 https://github.com\n```\n\n### 修改服务\n可通过发送 `修改服务 <名称> <参数名> <参数内容>` 以修改服务的参数\n* 不同协议支持修改的参数字段不同，具体请参考[协议支持](#协议支持)\n```\n修改服务 git截图 proxies http://127.0.0.1:10809\n```\n\n### 群组服务\n\n当多个API共同支持某项服务时，可通过 `群组服务 <名称1> <名称2> <群组名称>` 群组多个服务为一个显示\n\n* 只有当群组中的所有服务都为可用状态时，群组才显示为可用，当有一个或多个服务为故障状态时，群组都显示为故障\n\n例：假设当前已设置好 涩图信息API 和 涩图图床 两个服务，可通过下列命令组合为一个服务\n```\n群组服务 涩图信息API 涩图图床 涩图\n```\n群组命令前：\n```\nO 可用 | 涩图信息API\nX 故障 | 涩图图床\n```\n群组命令后：\n```\nX 故障 | 涩图\n```\n\n### 解散群组\n\n当需要解散群组时，可通过 `解散群组 <群组名称>` 解散\n\n* 解散群组后，群组内的服务都会重新作为独立服务显示在状态列表中\n\n```\n解散群组 涩图\n```\n\n### 删除服务\n可通过发送 `删除服务 <名称>` 以不再监测该服务\n```\n删除服务 git截图\n```\n\n### 群组操作\n在名称参数中加入转义符 `@` 以指定群组中的服务\n\n* 若群组或服务名中本身包含了转义符`@`，则需要通过`@@`以代替名称中的`@`\n\n例：在群组`涩图`中修改服务`涩图图床`的参数`timeout`为3\n```\n修改服务 涩图@涩图图床 timeout 3\n```\n\n\n## 协议支持\n\n以下是项目当前支持的协议，以及可被通过修改命令配置的字段\n\n### HTTP GET\n- 协议名称：`HTTP`\n- [x] 状态查询：探测地址超时前返回状态 200 为可用\n- [x] 服务名称：`name` @ [str]\n- [x] 监测地址：`host` @ [str]\n- [x] 超时时间：`timeout` @ [int]\n- [x] 代理地址：`proxies` @ [str, None]\n- [ ] 请求头：暂未支持\n- [ ] UA：暂未支持\n- [ ] Cookie：暂未支持\n- [ ] 有效响应码：暂未支持\n- [ ] 内容正则判定：暂未支持\n\n### TCP\n- 协议名称：`TCP`\n- [x] 状态查询：探测地址超时前成功建立连接为可用\n- [x] 服务名称：`name` @ [str]\n- [x] 监测地址：`host` @ [str]\n- [x] 端口：`port` @ [int]\n- [x] 超时时间：`timeout` @ [int]\n- [ ] 代理地址：暂未支持\n\n### PING\n- [ ] 状态查询：暂未支持\n- [ ] 监测地址：暂未支持\n- [ ] 代理地址：暂未支持\n- [ ] 超时时间：暂未支持\n\n\n## 添加协议\n\n### 说明\n**本段内容面向开发者，如不理解可跳过本段** \n\n若某项服务可用需要特殊的可用性检查逻辑，且无法通过通用协议支持实现（如动态解析内容并获取链接跳转）或当前协议暂未支持该判定特性时，可通过添加新的协议快速实现\n\n### 编写\n项目`.\\protocol`中内置了一个demo协议\n[demo.py](https://github.com/OREOCODEDEV/nonebot-plugin-servicestate/blob/main/nonebot_plugin_servicestate/protocol/demo.py)\n实现了一个可用概率为随机的协议，你可以参照内部的注释，编写自己的自定义协议方法\n\n下列步骤中默认均按照demo协议编写，如需要自定义协议请按照实际情况操作\n\n### 注册\n在`.\\protocol\\__init__.py`中导入需要注册的demo协议\n```\nfrom .demo import DEMOProtocol\n```\n\n### 使用\n现在，你已经完成自定义协议的所有步骤，可直接使用你的自定义协议了\n\n添加demo协议命令：`添加服务 DemoProtocol DemoName demo_url`\n\n修改随机可用概率为 25% ：`修改服务 DemoName normal_rate 25`\n\n修改为永远故障状态：`修改服务 DemoName always_malfunction True`\n\n使用上述命令并分别通过`服务状态`命令观察它们执行后的变化吧！\n\n\n\n## Todo\n- [x] 核心pydantic支持\n- [ ] 支持更多配置字段\n- [ ] 协议配置项合法检查接口支持\n- [ ] 协议载入配置方法统一实现\n- [ ] 协议必填配置项接口支持\n- [ ] 鲁棒性增强\n- [ ] 群组~~增删~~查改支持\n- [ ] OneBotV11配置文件收发\n- [ ] 不同用户服务绑定支持（咕咕咕\n- [ ] 还有上面一大堆协议中暂未支持的内容\n',
    'author': 'OREOCODEDEV',
    'author_email': '17620745509@126.COM',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/OREOCODEDEV/nonebot-plugin-servicestate',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

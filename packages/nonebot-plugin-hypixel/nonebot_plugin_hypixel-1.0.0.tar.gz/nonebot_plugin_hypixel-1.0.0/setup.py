import setuptools


with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="nonebot_plugin_hypixel",
    version="1.0.0",
    author="Sky_Dynamic",
    author_email="SkyDynamic@outlook.com",
    keywords=["pip", "nonebot2", "nonebot", "nonebot_plugin", "hypixel"],
    description="""基于OneBot适配器的NoneBot2获取Mineceaft最大的小游戏服务器Hypixel的玩家数据的插件""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SkyDynamic/nonebot_plugin_hypixel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=['nonebot2>=2.0.0rc1','nonebot-adapter-onebot>=2.1.5'],
    python_requires=">=3.7.3"
)
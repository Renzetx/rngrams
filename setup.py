import re
from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r if i.strip()]

with open("pyrogram/__init__.py", encoding="utf-8") as f:
    version = re.findall(r'__version__ = "(.+)"', f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="RNGram",
    version=version,
    description="Telegram MTProto API Framework in Python (Pyrogram Fork v2.5.1.1 + Pyromod)",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/renzetx/RNGram",
    author="WannnV",
    author_email="renboysid@gmail.com",
    license="LGPLv3",
    python_requires=">=3.9",
    packages=find_packages(exclude=["compiler*", "tests*"]),
    zip_safe=False,
    install_requires=requires
)

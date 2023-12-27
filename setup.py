import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webapp_builder",
    version="0.0.1",
    author="George Mountain",
    author_email="georgejiokem@gmail.com",
    description="Webapp Builder -- LLM/LVM Code Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/george-mountain/web-app-builder--LLM/archive/refs/tags/0.01.zip",
    project_urls={
        "Bug Tracker": "https://github.com/george-mountain/web-app-builder--LLM.git/issues"
    },
    license="MIT",
    packages=["webapp_builder"],
    install_requires=[
        "requests",
        "python-dotenv",
        "langchain",
        "transformers",
        "openai",
        "Pillow",
        "streamlit",
    ],
)

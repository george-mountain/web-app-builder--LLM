import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webapp_builder",
    version="1.1",
    author="George Mountain",
    author_email="engrmountain@gmail.com",
    description="Webapp Builder -- LLM/LVM Code Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/george-mountain/web-app-builder--LLM",
    project_urls={
        "Bug Tracker": "https://github.com/george-mountain/web-app-builder--LLM/issues"
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
    keywords=[
        "pypi",
        "llm",
        "lvm",
        "large language model",
        "large vision model",
        "code generator",
        "web app builder",
        "AI",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    download_url="https://github.com/george-mountain/web-app-builder--LLM/archive/refs/tags/1.1.tar.gz",
)

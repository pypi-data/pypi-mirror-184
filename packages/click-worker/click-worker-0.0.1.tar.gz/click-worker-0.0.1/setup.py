import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="click-worker",
    version="0.0.1",
    author="sAmurai_jack",
    author_email="spamersden555@gmail.com",
    description=("click worker is event invoking app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samuraijack9005/click-worker",
    project_urls={
        "Bug Tracker": "https://github.com/samuraijack9005/click-worker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pyautogui"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "click = clicker.cli:main",
        ]
    }
)
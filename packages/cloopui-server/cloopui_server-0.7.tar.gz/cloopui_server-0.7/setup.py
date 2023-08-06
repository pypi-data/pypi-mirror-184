import setuptools


setuptools.setup(
    name="cloopui_server",
    version="0.7",
    author="Francis B. Lavoie",
    author_email="francis.b.lavoie@usherbrooke.ca",
    description="Fast DB handler",
    long_description="Fast DB handler",
    long_description_content_type="text/markdown",
    url="https://catalyseur.ca",
    packages=setuptools.find_packages(),
    install_requires = ["mariadb","pyodbc"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points = {
        'console_scripts': ['cloopui_server=cloopui_server.command_line:main'],
    }
)
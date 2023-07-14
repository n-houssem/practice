from setuptools import find_packages, setup
def get_requirements(filepath):
    requirements=[]
    with open(filepath, "r") as file:
        req = file.readlines()
        requirements=[re.replace("\n","") for re in req if re!="-e ."]
    return requirements
setup(
    name="practiceproj",
    version="0.1",
    author="lhash",
    author_email="nhoussem32@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements("requirements.txt")
)
from setuptools import setup, find_packages

setup(
    name="Mahiru",
    version="1.0.0",
    author="Yash Kumar",
    description="Python AI Virtual Assistant",
    packages=find_packages(),
    install_requires=[
        "SpeechRecognition",
        "pyttsx3",
        "pandas",
        "nltk",
        "prompt_toolkit",
    ],
)
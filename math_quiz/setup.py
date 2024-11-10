from setuptools import setup, find_packages

setup(
    name="math_quiz",  # Package name
    version="0.1",  # Version of your package
    packages=find_packages(),  # Finds all packages (folders with __init__.py)
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',  # Links command to function
        ],
    },
    author="Faizan Nabi",  # Your name
    author_email="faizan.nabi202@gmail.com",  # Your email
    description="A simple math quiz game",  # Short description
    long_description=open('README.md').read(),  # Read README.md for detailed description
    long_description_content_type="text/markdown",  # Content type of README file
    url="https://github.com/Faizan-Nabi/-Faizan_Nabi_dsss_homework_2",  # Link to your GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version
)

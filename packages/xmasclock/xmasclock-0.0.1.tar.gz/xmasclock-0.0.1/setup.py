import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='xmasclock',
    version='0.0.1',
    description='Countdown until Christmas executable',
    author='Jacob Armentrout',
    long_description=long_description,
    long_description_context_type='text/markdown',
    scripts=['xmasclock/xmasclock.py'],
    url='https://github.com/SirJakesalot/xmasclock.git',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)

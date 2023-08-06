from setuptools import setup

setup(
        name='lwksprefs',
        version='0.1',
        description='Lightworks NLE preferences reader',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://gitlab.com/marcinjn/lwksprefs',
        author='Marcin Nowak',
        author_email='marcin.j.nowak@gmail.com',
        keywords='lwks lightworks parser',
        py_modules=['lwksprefs'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.7',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: POSIX :: Linux',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ]
)

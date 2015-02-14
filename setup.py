from distutils.core import setup
import os

setup(
    name='pdf-redact-tools',
    version='0.1',
    author='Micah Lee',
    author_email='micah.lee@firstlook.org',
    platforms=['GNU/Linux'],
    license='GPLv3',
    url='https://github.com/micahflee/pdf-redact-tools',
    description='PDF Redact Tools helps with securely redacting and stripping metadata from documents before publishing',
    long_description="PDF Redact Tools helps with securely redacting and stripping metadata from documents before publishing.",
    scripts=['pdf-redact-tools']
)

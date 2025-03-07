from setuptools import setup, find_packages

setup(
    name='coreui_django_component',
    version='0.0.1',    
    description='A Django package with reusable UI components using django-viewcomponent and optimized with django-compressor.',
    url='https://github.com/6F-TECH-CONSULTANT-INDIA-Pvt-Ltd/coreui_django_component',
    author='6F-TECH-CONSULTANT-INDIA-Pvt-Ltd',
    author_email='support@6ftechconsultant.com',
    license='MIT license',
    packages=find_packages(where="src"),  # Ensure correct package discovery
    package_dir={"": "src"},  # Assumes you are using a `src/` layout
    include_package_data=True,
    install_requires= [
        "django>=3.2",
        "django-viewcomponent",
        "django-compressor",                   
    ],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

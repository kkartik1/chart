from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Visualization',
    url='https://github.optum.com/kkartik1/RightPay/tree/main/Visualization',
    author='Kanishka Kartikeya',
    author_email='kanishka.kartikeya@optum.com',
    # Needed to actually package something
    packages=['BarChart', 'LineChart', 'PieChart', 'ScatterPlot', 'HeatMap', 'BoxWhiskers', 'GeoPlot'],
    # Needed for dependencies
    install_requires=['altair-data-server==0.4.1', 'altair-viewer==0.4.0', 'altair==4.1.0'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
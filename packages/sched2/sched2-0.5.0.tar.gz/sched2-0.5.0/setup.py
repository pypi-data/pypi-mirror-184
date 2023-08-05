# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['sched2']
setup_kwargs = {
    'name': 'sched2',
    'version': '0.5.0',
    'description': 'Event scheduler 2',
    'long_description': 'The `sched2` module provides a simple and intuitive way to schedule the execution of code in Python. For example, it allows you to schedule a function to be called at a specific time or after a particular delay or to schedule a function to be called repeatedly at a specific time interval. This can be useful for automating tasks or scheduling the execution of code without having to write your own scheduling logic. In addition, it is lightweight and easy to use, making it an excellent choice for scheduling the execution of code in Python.\n\n`sched2` implements a subclass of the `sched.scheduler` class from Python\'s standard library that adds additional functionality. This means that `sched2` includes all of the features and functionality of the `sched` module and adds extra methods. As a result, you can use `sched2` in place of `sched` in your code without any further modifications, and you will have access to the additional features provided by `sched2`. These other features include the `repeat` method and the `every` decorator, which allow you to repeatedly schedule a function to be called at a specific time interval.\n\n# Functionality\n- Schedule the execution of code at specific times or intervals\n- Schedule repeat function calls at specific time intervals\n- Simple and intuitive interface for scheduling code\n- Lightweight and easy to use\n- No external dependencies\n\n# Install\n\nTo install the sched2 module, you can use pip, the package installer for Python. Open a terminal and run the following command:\n\n```bash\npip install sched2\n```\n\n# Examples\n\nThe code bellow defines a function that checks if the IP address has changed and prints a message if it has. Then it creates an instance of a scheduler class and uses the `repeat` method to schedule the IP check function to run every two minutes. Finally, it starts the scheduler, so the IP check function will run indefinitely.\n\n```python\nfrom urllib.request import urlopen\nfrom sched2 import scheduler\n\n\ndef check_ip():\n    # Get the public IP address\n    global current_ip\n    ip = urlopen("https://icanhazip.com/").read().decode("utf-8").strip()\n\n    # Check if the IP address has changed\n    if ip != current_ip:\n        current_ip = ip\n        print(f"IP changed to {ip}")\n\n\n# Initialize the current_ip variable to None\ncurrent_ip = None\n\n# Create a scheduler\nsc = scheduler()\n\n# Run the check_ip function every 120 seconds\nsc.repeat(120, 1, check_ip)\n\n# Run the scheduler\nsc.run()\n```\n\nThe following code creates an instance of a scheduler class and decorates a function, so it runs every two minutes. First, the decorated function gets the public IP address and checks if it has changed. If it has, it updates and prints a message. Finally, it starts the scheduler, so the decorated function runs indefinitely.\n\n```python\nfrom urllib.request import urlopen\nfrom sched2 import scheduler\n\n# Create a scheduler\nsc = scheduler()\n\n\n@sc.every(120)  # Run every two minutes\ndef check_ip():\n    # Get the public IP address and check if it has changed\n    global current_ip\n    ip = urlopen("https://icanhazip.com/").read().decode("utf-8").strip()\n    if ip != current_ip:\n        current_ip = ip\n        print(f"IP changed to {ip}")\n\n\n# Initialize the current_ip variable to None\ncurrent_ip = None\n\n# Run the scheduler\nsc.run()\n```\n',
    'author': 'Pedro Rodrigues',
    'author_email': 'me@pdbr.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/medecau/sched2',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

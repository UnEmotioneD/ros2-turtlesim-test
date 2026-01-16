from setuptools import find_packages, setup

PACKAGE_NAME = "my_first_package"

setup(
    name=PACKAGE_NAME,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + PACKAGE_NAME]),
        ("share/" + PACKAGE_NAME, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Lemon",
    maintainer_email="blackeagle10@icloud.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        # node's main method path
        "console_scripts": [
            # executable_name = pkg_name.file_name:function_name
            "my_subscriber = my_first_package.my_subscriber:main",
            "my_publisher = my_first_package.my_publisher:main",
            "turtle_cmd_and_pose = my_first_package.turtle_cmd_and_pose:main",
            "my_service_server = my_first_package.my_service_server:main",
            "dist_turtle_action_server = my_first_package.dist_turtle_action_server:main",
            "my_multi_thread = my_first_package.my_multi_thread:main",
        ],
    },
)

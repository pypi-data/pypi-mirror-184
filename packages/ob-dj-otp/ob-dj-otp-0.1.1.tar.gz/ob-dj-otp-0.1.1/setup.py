from setuptools import setup

# version = "0.0.3"

setup(
    install_requires=[
        "django",
        "djangorestframework",
    ],
    # TODO: https://github.com/obytes/ob-dj-otp/issues/3
    packages=[
        "ob_dj_otp.apis",
        "ob_dj_otp.apis.otp",
        "ob_dj_otp.core",
        "ob_dj_otp.core.otp",
        "ob_dj_otp.utils",
    ],
    tests_require=["pytest"],
    use_scm_version={
        "write_to": "version.py",
    },
    setup_requires=["setuptools_scm"],
)

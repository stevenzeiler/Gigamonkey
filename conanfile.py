from conans import ConanFile

class ConanPackage(ConanFile):
    name = 'gigamonkey'
    version = "0.1.0"

    generators = 'cmake_find_package'

    requires = [
        ('cryptopp/8.5.0'),
    ]

    default_options = (
        'boost:shared=False',
    )

from conans import ConanFile

class ConanPackage(ConanFile):
    name = 'gigamonkey'
    version = "0.1.0"

    generators = ['cmake', 'cmake_find_package']

    requires = [
        ('boost/1.76.0'),
        ('cryptopp/8.5.0'),
        ('nlohmann_json/3.2.0'),
        ('gmp/6.2.1'),
        #(github.com/bitcoin-sv/bitcoin-sv)
        #(github.com/bitcoin-core/secp256k1)
    ]

    default_options = (
        'boost:shared=False',
    )

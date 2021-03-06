# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

class RocmBandwidthTest(CMakePackage):
    """Test to measure PciE bandwidth on ROCm platforms"""

    homepage = "https://github.com/RadeonOpenCompute/rocm_bandwidth_test"
    url      = "https://github.com/RadeonOpenCompute/rocm_bandwidth_test/archive/rocm-3.5.0.tar.gz"

    maintainers = ['srekolam', 'arjun-raj-kuppala']

    version('3.5.0', sha256='fbb63fb8713617fd167d9c1501acbd92a6b189ee8e1a8aed668fa6666baae389')

    variant('build_type', default='Release', values=("Release", "Debug"), description='CMake build type')

    depends_on('cmake@3.5.2', type='build')
    depends_on('hsa-rocr-dev@3.5:', type='link', when='@3.5:')
    depends_on('hsakmt-roct@3.5:', type='build', when='@3.5:')

    build_targets = ['package']

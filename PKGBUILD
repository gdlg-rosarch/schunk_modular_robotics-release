# Script generated with Bloom
pkgdesc="ROS - This stack includes packages that provide access to the Schunk hardware through ROS messages, services and actions."
url='http://ros.org/wiki/schunk_modular_robotics'

pkgname='ros-kinetic-schunk-modular-robotics'
pkgver='0.6.10_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-schunk-description'
'ros-kinetic-schunk-libm5api'
'ros-kinetic-schunk-powercube-chain'
'ros-kinetic-schunk-sdh'
'ros-kinetic-schunk-simulated-tactile-sensors'
)

conflicts=()
replaces=()

_dir=schunk_modular_robotics
source=()
md5sums=()

prepare() {
    cp -R $startdir/schunk_modular_robotics $srcdir/schunk_modular_robotics
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}


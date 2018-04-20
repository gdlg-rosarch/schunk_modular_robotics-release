# Script generated with Bloom
pkgdesc="ROS - This package contains the description (mechanical, kinematic, visual, etc.) of different schunk components. The files in this package are parsed and used by a variety of other components. Most users will not interact directly with this package."
url='http://ros.org/wiki/schunk_description'

pkgname='ros-kinetic-schunk-description'
pkgver='0.6.10_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('gtest'
'ros-kinetic-catkin'
)

depends=('ros-kinetic-gazebo-ros'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=schunk_description
source=()
md5sums=()

prepare() {
    cp -R $startdir/schunk_description $srcdir/schunk_description
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


# Script generated with Bloom
pkgdesc="ROS - This package wraps the libm5api to use it as a ros dependency. Original sources from http://www.schunk-modular-robotics.com/fileadmin/user_upload/software/schunk_libm5api_source.zip."
url='http://ros.org/wiki/schunk_libm5api'

pkgname='ros-kinetic-schunk-libm5api'
pkgver='0.6.10_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-libntcan'
'ros-kinetic-libpcan'
)

depends=('ros-kinetic-libntcan'
'ros-kinetic-libpcan'
)

conflicts=()
replaces=()

_dir=schunk_libm5api
source=()
md5sums=()

prepare() {
    cp -R $startdir/schunk_libm5api $srcdir/schunk_libm5api
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


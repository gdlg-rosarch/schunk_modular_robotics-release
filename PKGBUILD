# Script generated with Bloom
pkgdesc="ROS - This package provides an interface for operating the schunk dexterous hand (SDH), including the tactile sensors."
url='http://ros.org/wiki/schunk_sdh'

pkgname='ros-kinetic-schunk-sdh'
pkgver='0.6.10_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'dpkg'
'libusb-compat'
'ros-kinetic-actionlib'
'ros-kinetic-catkin'
'ros-kinetic-cob-srvs'
'ros-kinetic-control-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-libntcan'
'ros-kinetic-libpcan'
'ros-kinetic-message-generation'
'ros-kinetic-roscpp'
'ros-kinetic-roslint'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
)

depends=('boost'
'dpkg'
'libusb-compat'
'ros-kinetic-actionlib'
'ros-kinetic-cob-srvs'
'ros-kinetic-control-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-libntcan'
'ros-kinetic-libpcan'
'ros-kinetic-message-runtime'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=schunk_sdh
source=()
md5sums=()

prepare() {
    cp -R $startdir/schunk_sdh $srcdir/schunk_sdh
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


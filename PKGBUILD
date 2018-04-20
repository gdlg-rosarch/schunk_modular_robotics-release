# Script generated with Bloom
pkgdesc="ROS - This packages provides a configurable driver of a chain of Schunk powercubes. The powercube chain is configured through parameters. Most users will not directly interact with this package but with the corresponding launch files in other packages, e.g. schunk_bringup, cob_bringup, ..."
url='http://ros.org/wiki/schunk_powercube_chain'

pkgname='ros-kinetic-schunk-powercube-chain'
pkgver='0.6.10_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('linux-headers'
'ros-kinetic-catkin'
'ros-kinetic-cob-srvs'
'ros-kinetic-control-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-libntcan'
'ros-kinetic-libpcan'
'ros-kinetic-roscpp'
'ros-kinetic-schunk-libm5api'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
)

depends=('linux-headers'
'ros-kinetic-cob-srvs'
'ros-kinetic-control-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-libntcan'
'ros-kinetic-libpcan'
'ros-kinetic-roscpp'
'ros-kinetic-schunk-libm5api'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=schunk_powercube_chain
source=()
md5sums=()

prepare() {
    cp -R $startdir/schunk_powercube_chain $srcdir/schunk_powercube_chain
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


# Script generated with Bloom
pkgdesc="ROS - This package provides simulated tactile sensors for the Schunk Dextrous Hand (SDH) which is mounted on the Care-O-bot arm. The node subscribes to the Gazebo bumper topics of the SDH. It transforms the Gazebo feedback to the &quot;tactile_data&quot; topic to provide the same tactile sensor interface as the schunk_sdh package. The following parameters can be set: * cells_x: The number of patches on the tactile sensor in the direction perpendicular to the finger. Defaults to 6. * cells_y: The number of patches on the tactile sensor along the direction of the finger. Defaults to 14. * output_range: The maximum output value of one patch. Defaults to 3500. * sensitivity: The change of output in one patch per Newton. Defaults to 350. The sensitivity can be approximated by the following formula: S = output_range / (measurement_range * cell_area) - The measurement range of the tactile pads is 250 kPa (from the data sheet). - The output range can be determined by experiment from the real SDH. It is about 3500. - The cell area is the size of one patch. Length and width of the area are determined by dividing the length/width of the collision surface by the number of cells in the respective direction. Important: In most cases this is NOT the cell area that is given in the data sheet! * filter_length: The length of the moving average filter which smoothes the values from simulation. Defaults to 10. The node subscribes to the following topics to receive data from the simulation: * thumb_2/state * thumb_3/state * finger_12/state * finger_13/state * finger_22/state * finger_23/state The node publishes the processed data on the following topic: * tactile_data The simulated bumper must obtain the collision data in the link that the sensor is attached to. This is achieved by setting the &quot;frameName&quot; property in the gazebo_ros_bumper controller."
url='http://ros.org/wiki/schunk_simulated_tactile_sensors'

pkgname='ros-kinetic-schunk-simulated-tactile-sensors'
pkgver='0.6.10_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-gazebo-msgs'
'ros-kinetic-rospy'
'ros-kinetic-schunk-sdh'
)

conflicts=()
replaces=()

_dir=schunk_simulated_tactile_sensors
source=()
md5sums=()

prepare() {
    cp -R $startdir/schunk_simulated_tactile_sensors $srcdir/schunk_simulated_tactile_sensors
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


Name:           ros-kinetic-schunk-simulated-tactile-sensors
Version:        0.6.10
Release:        0%{?dist}
Summary:        ROS schunk_simulated_tactile_sensors package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/schunk_simulated_tactile_sensors
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-gazebo-msgs
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-schunk-sdh
BuildRequires:  ros-kinetic-catkin

%description
This package provides simulated tactile sensors for the Schunk Dextrous Hand
(SDH) which is mounted on the Care-O-bot arm. The node subscribes to the Gazebo
bumper topics of the SDH. It transforms the Gazebo feedback to the
&quot;tactile_data&quot; topic to provide the same tactile sensor interface as
the schunk_sdh package. The following parameters can be set: * cells_x: The
number of patches on the tactile sensor in the direction perpendicular to the
finger. Defaults to 6. * cells_y: The number of patches on the tactile sensor
along the direction of the finger. Defaults to 14. * output_range: The maximum
output value of one patch. Defaults to 3500. * sensitivity: The change of output
in one patch per Newton. Defaults to 350. The sensitivity can be approximated by
the following formula: S = output_range / (measurement_range * cell_area) - The
measurement range of the tactile pads is 250 kPa (from the data sheet). - The
output range can be determined by experiment from the real SDH. It is about
3500. - The cell area is the size of one patch. Length and width of the area are
determined by dividing the length/width of the collision surface by the number
of cells in the respective direction. Important: In most cases this is NOT the
cell area that is given in the data sheet! * filter_length: The length of the
moving average filter which smoothes the values from simulation. Defaults to 10.
The node subscribes to the following topics to receive data from the simulation:
* thumb_2/state * thumb_3/state * finger_12/state * finger_13/state *
finger_22/state * finger_23/state The node publishes the processed data on the
following topic: * tactile_data The simulated bumper must obtain the collision
data in the link that the sensor is attached to. This is achieved by setting the
&quot;frameName&quot; property in the gazebo_ros_bumper controller.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Jan 07 2018 Bruno Brito <bfb@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

* Wed Jul 19 2017 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.9-0
- Autogenerated by Bloom


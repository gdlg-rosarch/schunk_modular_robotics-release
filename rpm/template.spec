Name:           ros-indigo-schunk-sdh
Version:        0.5.6
Release:        4%{?dist}
Summary:        ROS schunk_sdh package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/schunk_sdh
Source0:        %{name}-%{version}.tar.gz

Requires:       libusb-devel
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-brics-actuator
Requires:       ros-indigo-cob-srvs
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-libntcan
Requires:       ros-indigo-libpcan
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-urdf
BuildRequires:  dpkg
BuildRequires:  libusb-devel
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-brics-actuator
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-srvs
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-libntcan
BuildRequires:  ros-indigo-libpcan
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-urdf

%description
This package provides an interface for operating the schunk dexterous hand
(SDH), including the tactile sensors.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Aug 27 2014 Mathias Luedtke <mdl@ipa.fhg.de> - 0.5.6-4
- Autogenerated by Bloom

* Wed Aug 27 2014 Mathias Luedtke <mdl@ipa.fhg.de> - 0.5.6-3
- Autogenerated by Bloom

* Wed Aug 27 2014 Mathias Luedtke <mdl@ipa.fhg.de> - 0.5.6-2
- Autogenerated by Bloom

* Wed Aug 27 2014 Mathias Luedtke <mdl@ipa.fhg.de> - 0.5.6-1
- Autogenerated by Bloom

* Wed Aug 27 2014 Mathias Luedtke <mdl@ipa.fhg.de> - 0.5.6-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Mathias Luedtke <mdl@ipa.fhg.de> - 0.5.5-0
- Autogenerated by Bloom


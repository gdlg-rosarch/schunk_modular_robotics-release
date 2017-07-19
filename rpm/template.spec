Name:           ros-kinetic-schunk-description
Version:        0.6.9
Release:        0%{?dist}
Summary:        ROS schunk_description package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/schunk_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-gazebo-ros
Requires:       ros-kinetic-xacro
BuildRequires:  gtest-devel
BuildRequires:  ros-kinetic-catkin

%description
This package contains the description (mechanical, kinematic, visual, etc.) of
different schunk components. The files in this package are parsed and used by a
variety of other components. Most users will not interact directly with this
package.

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
* Wed Jul 19 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.9-0
- Autogenerated by Bloom


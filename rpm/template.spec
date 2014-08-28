Name:           ros-indigo-schunk-description
Version:        0.5.7
Release:        2%{?dist}
Summary:        ROS schunk_description package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/schunk_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gazebo-ros
BuildRequires:  gtest-devel
BuildRequires:  ros-indigo-catkin

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
* Thu Aug 28 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.7-2
- Autogenerated by Bloom

* Wed Aug 27 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.6-4
- Autogenerated by Bloom

* Wed Aug 27 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.6-3
- Autogenerated by Bloom

* Wed Aug 27 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.6-2
- Autogenerated by Bloom

* Wed Aug 27 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.6-1
- Autogenerated by Bloom

* Wed Aug 27 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.6-0
- Autogenerated by Bloom

* Wed Aug 27 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.7-0
- Autogenerated by Bloom

* Wed Aug 27 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.7-1
- Autogenerated by Bloom

* Tue Aug 26 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.5-0
- Autogenerated by Bloom


Name:           ros-indigo-schunk-libm5api
Version:        0.5.6
Release:        3%{?dist}
Summary:        ROS schunk_libm5api package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/schunk_libm5api
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-libntcan
Requires:       ros-indigo-libpcan
Requires:       ros-indigo-roslib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-libntcan
BuildRequires:  ros-indigo-libpcan
BuildRequires:  ros-indigo-roslib

%description
This package wraps the libm5api to use it as a ros dependency. Original sources
from http://www.schunk-modular-
robotics.com/fileadmin/user_upload/software/schunk_libm5api_source.zip.

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
* Wed Aug 27 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.5.6-3
- Autogenerated by Bloom

* Wed Aug 27 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.5.6-2
- Autogenerated by Bloom

* Wed Aug 27 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.5.6-1
- Autogenerated by Bloom

* Wed Aug 27 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.5.6-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.5.5-0
- Autogenerated by Bloom


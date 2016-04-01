Name:           ros-indigo-schunk-powercube-chain
Version:        0.6.7
Release:        0%{?dist}
Summary:        ROS schunk_powercube_chain package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/schunk_powercube_chain
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cob-srvs
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-libntcan
Requires:       ros-indigo-libpcan
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-schunk-libm5api
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-urdf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-srvs
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-libntcan
BuildRequires:  ros-indigo-libpcan
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-schunk-libm5api
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-urdf

%description
This packages provides a configurable driver of a chain of Schunk powercubes.
The powercube chain is configured through parameters. Most users will not
directly interact with this package but with the corresponding launch files in
other packages, e.g. schunk_bringup, cob_bringup, ...

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Apr 01 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Tue Sep 01 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom


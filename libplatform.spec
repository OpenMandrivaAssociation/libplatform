#
# spec file for package libplatform
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _SO_nr 1_0
Name:           libplatform
Version:        1.0.10
Release:        1.1
Summary:        Platform support library used by libCEC and binary add-ons for Kodi
License:        GPL-2.0+
Group:          Hardware/TV
Url:            https://github.com/Pulse-Eight/platform
Source:         https://github.com/Pulse-Eight/platform/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Platform support library used by libCEC and binary add-ons for Kodi.

%package -n %{name}%{_SO_nr}
Summary:        Platform support library used by libCEC and binary add-ons for Kodi
Group:          Hardware/TV

%description -n %{name}%{_SO_nr}
Platform support library used by libCEC and binary add-ons for Kodi.

%package devel
Summary:        Platform support library used by libCEC development files
Group:          Development/Languages/C and C++
Requires:       %{name}%{_SO_nr} = %{version}

%description devel
Development files for platform support library used by libCEC.

%prep
%setup -q -n platform-%{version}

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post	-n %{name}%{_SO_nr} -p /sbin/ldconfig

%postun -n %{name}%{_SO_nr} -p /sbin/ldconfig

%files -n %{name}%{_SO_nr}
%defattr(-,root,root)
%{_libdir}/%{name}.so.%{version}
%{_libdir}/%{name}.so.1.0

%files devel
%defattr(-,root,root)
%{_libdir}/%{name}.so
%{_includedir}/platform/
%{_includedir}/platform/posix/
%{_includedir}/platform/sockets/
%{_includedir}/platform/threads/
%{_includedir}/platform/util/
%{_libdir}/pkgconfig/platform.pc
%{_libdir}/platform
%{_libdir}/platform/platform-config.cmake

%changelog
* Sat Jul 18 2015 mpluskal@suse.com
- Update to 1.0.10
  * fixed: posix socket return value for connect.
* Tue Jun  9 2015 mpluskal@suse.com
- Fix previous changelog entry
- Use url for source
- Use cmake macro
* Thu May 14 2015 sagiben@gmail.com
- platform 1.0.9-1
  * fixed: add missing stdio.h include in windows/os-socket.h
- platform 1.0.8-1
  * added: cdevsocket.h character device socket
  * fixed: guards for #defines on OS X and iOS for values already
    defined in
    CFPlugInCOM.h
- platform 1.0.7-1~trusty
  * fixed: include on OS X
- platform 1.0.6-1
  * fixed: add include path and link the threads lib
  * (re-)added: public Reset() function in CEvent
  * sync UseMultiArch.cmake
- platform 1.0.5-1
  * fixed: missing #include <string> in socket.h
- platform 1.0.4-1
  * proper platform.pc.in fix
- platform 1.0.3-1
  * platform.pc.in fix
- platform 1.0.2-1
  * Build fixes
- platform 1.0.0-1
  * Initial release

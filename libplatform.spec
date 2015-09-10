%define _SO_nr 1_0
%define debug_package %{nil}

Name:           libplatform
Version:        1.0.10
Release:        1
Summary:        Platform support library used by libCEC and binary add-ons for Kodi
License:        GPL-2.0+
Group:          Video
Url:            https://github.com/Pulse-Eight/platform
Source:         https://github.com/Pulse-Eight/platform/archive/%{version}.tar.gz
BuildRequires:  cmake
#Patch0:         platform-1.0.10-install.patch


%description
Platform support library used by libCEC and binary add-ons for Kodi.

%package -n %{name}%{_SO_nr}
Summary:        Platform support library used by libCEC and binary add-ons for Kodi
Group:          Video

%description -n %{name}%{_SO_nr}
Platform support library used by libCEC and binary add-ons for Kodi.

%package devel
Summary:        Platform support library used by libCEC development files
Group:          Development/C
Requires:       %{name}%{_SO_nr} = %{version}

%description devel
Development files for platform support library used by libCEC.

%prep
%setup -q -n platform-%{version}

%build
%cmake
%make

%install

#No Install file so do it manually
#dirs
install -d -m755 $RPM_BUILD_ROOT%{_libdir}/platform
install -d -m755 $RPM_BUILD_ROOT%{_includedir}/platform
install -d -m755 $RPM_BUILD_ROOT%{_includedir}/platform/posix
install -d -m755 $RPM_BUILD_ROOT%{_includedir}/platform/sockets
install -d -m755 $RPM_BUILD_ROOT%{_includedir}/platform/threads
install -d -m755 $RPM_BUILD_ROOT%{_includedir}/platform/util
#libs
install -m755 build/libplatform.so.1.0.10 $RPM_BUILD_ROOT%{_libdir}
install -m777 build/libplatform.so.1.0 $RPM_BUILD_ROOT%{_libdir}
install -m777 build/libplatform.so $RPM_BUILD_ROOT%{_libdir}
#include
install -m644 src/os.h $RPM_BUILD_ROOT%{_includedir}/platform
install -m644 src/posix/os-socket.h $RPM_BUILD_ROOT%{_includedir}/platform/posix
install -m644 src/posix/os-threads.h $RPM_BUILD_ROOT%{_includedir}/platform/posix
install -m644 src/posix/os-types.h $RPM_BUILD_ROOT%{_includedir}/platform/posix
install -m644 src/sockets/cdevsocket.h $RPM_BUILD_ROOT%{_includedir}/platform/sockets
install -m644 src/sockets/socket.h $RPM_BUILD_ROOT%{_includedir}/platform/sockets
install -m644 src/sockets/tcp.h $RPM_BUILD_ROOT%{_includedir}/platform/sockets
install -m644 src/threads/atomics.h $RPM_BUILD_ROOT%{_includedir}/platform/threads
install -m644 src/threads/mutex.h $RPM_BUILD_ROOT%{_includedir}/platform/threads
install -m644 src/threads/threads.h $RPM_BUILD_ROOT%{_includedir}/platform/threads
install -m644 src/util/StdString.h $RPM_BUILD_ROOT%{_includedir}/platform/util
install -m644 src/util/StringUtils.h $RPM_BUILD_ROOT%{_includedir}/platform/util
install -m644 src/util/atomic.h $RPM_BUILD_ROOT%{_includedir}/platform/util
install -m644 src/util/buffer.h $RPM_BUILD_ROOT%{_includedir}/platform/util
install -m644 src/util/timeutils.h $RPM_BUILD_ROOT%{_includedir}/platform/util
install -m644 src/util/util.h $RPM_BUILD_ROOT%{_includedir}/platform/util
install -m644 build/platform.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig
install -m644 build/platform-config.cmake $RPM_BUILD_ROOT%{_libdir}platform

%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files -n %{name}%{_SO_nr}
%{_libdir}/%{name}.so.%{version}
%{_libdir}/%{name}.so.1.0

%files devel
%{_libdir}/%{name}.so
%{_includedir}/platform/
%{_includedir}/platform/posix/
%{_includedir}/platform/sockets/
%{_includedir}/platform/threads/
%{_includedir}/platform/util/
%{_libdir}/pkgconfig/platform.pc
%{_libdir}/platform
%{_libdir}/platform/platform-config.cmake


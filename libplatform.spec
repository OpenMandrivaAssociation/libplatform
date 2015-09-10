%define _SO_nr 1_0

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
install -d -m755 $RPM_BUILD_ROOT/%{_libdir}/platform
install -d -m755 $RPM_BUILD_ROOT/%{_includedir}/platform
install -d -m755 $RPM_BUILD_ROOT/%{_includedir}/platform/posix
install -d -m755 $RPM_BUILD_ROOT/%{_includedir}/platform/sockets
install -d -m755 $RPM_BUILD_ROOT/%{_includedir}/platform/threads
install -d -m755 $RPM_BUILD_ROOT/%{_includedir}/platform/util
#libs
install -m755 libplatform.so.1.0.10 $RPM_BUILD_ROOT/%{_libdir}/libplatform.so.1.0.10
install -m777 libplatform.so.1.0 $RPM_BUILD_ROOT/%{_libdir}/libplatform.so.1.0
install -m777 libplatform.so $RPM_BUILD_ROOT/%{_libdir}/libplatform.so
#include
install -m644 src/os.h $RPM_BUILD_ROOT/%{_includedir}/platform/os.h
install -m644 src/posix/os-socket.h $RPM_BUILD_ROOT/%{_includedir}/platform/posix/os-socket.h
install -m644 src/posix/os-threads.h $RPM_BUILD_ROOT/%{_includedir}/platform/posix/os-threads.h
install -m644 src/posix/os-types.h $RPM_BUILD_ROOT/%{_includedir}/platform/posix/os-types.h
install -m644 src/sockets/cdevsocket.h $RPM_BUILD_ROOT/%{_includedir}/platform/sockets/cdevsocket.h
install -m644 src/sockets/socket.h $RPM_BUILD_ROOT/%{_includedir}/platform/sockets/socket.h
install -m644 src/sockets/tcp.h $RPM_BUILD_ROOT/%{_includedir}/platform/sockets/tcp.h
install -m644 src/threads/atomics.h $RPM_BUILD_ROOT/%{_includedir}/platform/threads/atomics.h
install -m644 src/threads/mutex.h $RPM_BUILD_ROOT/%{_includedir}/platform/threads/mutex.h
install -m644 src/threads/threads.h $RPM_BUILD_ROOT/%{_includedir}/platform/threads/threads.h
install -m644 src/util/StdString.h $RPM_BUILD_ROOT/%{_includedir}/platform/util/StdString.h
install -m644 src/util/StringUtils.h $RPM_BUILD_ROOT/%{_includedir}/platform/util/StringUtils.h
install -m644 src/util/atomic.h $RPM_BUILD_ROOT/%{_includedir}/platform/util/atomic.h
install -m644 src/util/buffer.h $RPM_BUILD_ROOT/%{_includedir}/platform/util/buffer.h
install -m644 src/util/timeutils.h $RPM_BUILD_ROOT/%{_includedir}/platform/util/timeutils.h
install -m644 src/util/util.h $RPM_BUILD_ROOT/%{_includedir}/platform/util/util.h
install -m644 platform.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/platform.pc
install -m644 platform-config.cmake $RPM_BUILD_ROOT/%{_libdir}platform/platform-config.cmake

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


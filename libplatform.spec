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
Patch0:         platform-1.0.10-install.patch


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
%patch0 -p0 -b .install

%build
%cmake
%make

%install
%make_install

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


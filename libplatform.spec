%define _SO_nr 1_0

Name:           libplatform
Version:        1.0.10
Release:        1
Summary:        Platform support library used by libCEC and binary add-ons for Kodi
License:        GPL-2.0+
Group:          Video
Url:            https://github.com/Pulse-Eight/platform
Source0:        https://github.com/Pulse-Eight/platform/archive/%{version}.tar.gz
Source1:	libplatform.rpmlintrc
BuildRequires:  cmake


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
rm -rf $RPM_BUILD_ROOT

%make_install -C build

%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files -n %{name}%{_SO_nr}
%{_libdir}/%{name}.so.%{version}
%{_libdir}/%{name}.so.1.0

%files devel
%{_libdir}/%{name}.so
%{_includedir}/platform/
%{_libdir}/pkgconfig/*
%{_libdir}/platform/

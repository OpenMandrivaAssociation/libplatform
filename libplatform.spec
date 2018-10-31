%define p8name libp8-platform
%define major 2
%define libname %mklibname p8-platform %{major}
%define devname %mklibname p8-platform -d

Name:           libplatform
Version:        2.1.0.1
Release:        2
Summary:        Platform support library used by libCEC and binary add-ons for Kodi
License:        GPL-2.0+
Group:          Video
Url:            https://github.com/Pulse-Eight/platform
Source0:	https://github.com/Pulse-Eight/platform/archive/p8-platform-%{version}.tar.gz
Source1:	libplatform.rpmlintrc
BuildRequires:  cmake


%description
Platform support library used by libCEC and binary add-ons for Kodi.

%package -n %{libname}
Summary:        Platform support library used by libCEC and binary add-ons for Kodi
Group:          Video

%description -n %{libname}
Platform support library used by libCEC and binary add-ons for Kodi.

%package -n	%{devname}
Summary:        Platform support library used by libCEC development files
Group:          Development/C
Requires:       %{libname} = %{version}

%description -n %{devname}
Development files for platform support library used by libCEC.

%prep
%setup -q -n platform-p8-platform-%{version}

%build
%cmake
%make

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/%{p8name}.so.%{major}*

%files -n %{devname}
%{_libdir}/%{p8name}.so
%{_includedir}/p8-platform/
%{_libdir}/pkgconfig/*
%{_libdir}/p8-platform/

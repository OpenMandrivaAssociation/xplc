%define name 	xplc
%define version 0.3.13
%define release %mkrel 6

%define major	0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %name

Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	LGPLv2+
Group:          System/Libraries
Group:          Development/C
Summary: 	Component system
URL: 		http://xplc.sourceforge.net
Source: 	http://downloads.sourceforge.net/xplc/%{name}-%{version}.tar.bz2
# Install devel libraries to /usr/lib and not /usr/lib/%name-%version
Patch0:		xplc-0.3.13-devel-location.patch
# rename uuidgen to xplc-uuidgen
Patch1:		xplc-0.3.13-uuidgen.patch
Patch2:		xplc-0.3.13-as-needed.patch
BuildRequires:	libext2fs-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
XPLC ("Cross-Platform Lightweight Components") is a component system that will
provide extensibility and reusability both inside and between applications, 
while being portable across platforms (and languages) and having the lowest 
possible overhead (both in machine resources and programming effort).

%package uuidgen
Group:		System/Libraries
Summary: 	Component system

%description uuidgen
XPLC ("Cross-Platform Lightweight Components") is a component system that will
provide extensibility and reusability both inside and between applications, 
while being portable across platforms (and languages) and having the lowest 
possible overhead (both in machine resources and programming effort). This
packages contains the UUID generation tools that are provided with XPLC. The
'uuidgen' tool is renamed 'xplc-uuidgen' to avoid conflict with the 'uuidgen'
tool in the e2fs-progs package.

%package -n %{libname}
Group:          System/Libraries
Summary: 	Component system

%description -n %{libname}
XPLC ("Cross-Platform Lightweight Components") is a component system that will
provide extensibility and reusability both inside and between applications, 
while being portable across platforms (and languages) and having the lowest 
possible overhead (both in machine resources and programming effort).

%package -n %{develname}
Summary: Development files for XPLC
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Obsoletes: %{mklibname -d xplc 0}

%description -n %{develname}
XPLC ("Cross-Platform Lightweight Components") is a component system that will
provide extensibility and reusability both inside and between applications, 
while being portable across platforms (and languages) and having the lowest 
possible overhead (both in machine resources and programming effort). This 
package contains the files needed for developing applications which use 
XPLC.

%prep
%setup -q
%patch0 -p1 -b .devel
%patch1 -p1 -b .uuid
%patch2 -p0 -b .needed

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files uuidgen
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*

%files -n %{libname}
%doc NEWS README TODO
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}-%{version}
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

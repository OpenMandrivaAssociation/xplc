%define major	0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %name

Name:		xplc
Version:	0.3.13
Release:	24
License: 	LGPLv2+
Group:		System/Libraries
Summary:	Component system
URL:		http://xplc.sourceforge.net
Source:		http://downloads.sourceforge.net/xplc/%{name}-%{version}.tar.bz2
Source100:	xplc.rpmlintrc
# Install devel libraries to /usr/lib and not /usr/lib/%name-%version
Patch0:		xplc-0.3.13-devel-location.patch
# rename uuidgen to xplc-uuidgen
Patch1:		xplc-0.3.13-uuidgen.patch
Patch2:		xplc-0.3.13-as-needed.patch
BuildRequires:	pkgconfig(ext2fs)

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
Group:		System/Libraries
Summary:	Component system

%description -n %{libname}
XPLC ("Cross-Platform Lightweight Components") is a component system that will
provide extensibility and reusability both inside and between applications, 
while being portable across platforms (and languages) and having the lowest 
possible overhead (both in machine resources and programming effort).

%package -n %{develname}
Summary:	Development files for XPLC
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

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
%makeinstall_std

%files uuidgen
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%doc NEWS README TODO
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}-%{version}
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.13-8mdv2011.0
+ Revision: 671355
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.13-7mdv2011.0
+ Revision: 608229
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.13-6mdv2010.1
+ Revision: 524460
- rebuilt for 2010.1

* Tue Aug 26 2008 Funda Wang <fwang@mandriva.org> 0.3.13-5mdv2009.0
+ Revision: 276310
- add patch fix building with newer ldflags
- new devel package policy

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3.13-3mdv2008.1
+ Revision: 171190
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Apr 27 2007 Adam Williamson <awilliamson@mandriva.org> 0.3.13-2mdv2008.0
+ Revision: 18534
- fix lib naming (blino)

* Thu Apr 26 2007 Adam Williamson <awilliamson@mandriva.org> 0.3.13-1mdv2008.0
+ Revision: 18432
- Import xplc


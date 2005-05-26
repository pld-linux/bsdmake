Summary:	BSD make program.
Name:		bsdmake
Version:	11
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://www.opensource.apple.com/darwinsource/tarballs/other/%{name}-%{version}.tar.gz
# Source0-md5:	c2c2fe0c1f28bead4827ced0ef1cccee
URL:		http://www.opensource.apple.com/darwinsource/10.3.9/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BSD make program.

%prep
%setup -q 

%build
%{__cc} -DDEFSHELL=1 -Dlint -I. -c *.c
cd lst.lib; %{__cc} -I.. -Dlint -c *.c
cd ..
%{__cc} *.o lst.lib/*.o -o bsdmake

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/mk
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install bsdmake $RPM_BUILD_ROOT%{_bindir}
install make.1 $RPM_BUILD_ROOT%{_mandir}/man1/bsdmake.1
cp -rf mk/*  $RPM_BUILD_ROOT%{_datadir}/mk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc mk/bsd.README
%attr(755,root,root) %{_bindir}/bsdmake
%dir %{_datadir}/mk
%{_datadir}/mk/*.mk
%{_mandir}/man1/*

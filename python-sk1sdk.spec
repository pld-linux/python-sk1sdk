# NOTE: includes a copy of tkinter + aux extensions (ttk, tkimage)
Summary:	Set of Python GUI extensions for sK1 Project
Summary(pl.UTF-8):	Zbiór pythonowych rozszerzeń GUI dla projektu sK1
Name:		python-sk1sdk
Version:	0.9.1
%define	subver	pre2
Release:	0.%{subver}.1
License:	LGPL v2+
Group:		Libraries/Python
Source0:	https://sk1.googlecode.com/files/sk1sdk-%{version}%{subver}_rev1383.tar.gz
# Source0-md5:	b6db1a14ed9d39251851a3d78b63bb15
URL:		http://sk1project.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tcl-devel >= 8.5
BuildRequires:	tk-devel >= 8.5
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	zlib-devel
Requires:	python-libs
Requires:	python-sk1libs >= 0.9.1
Suggests:	fonts-TTF-bitstream-vera
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of Python GUI extensions for sK1 Project.

%description -l pl.UTF-8
Zbiór pythonowych rozszerzeń GUI dla projektu sK1.

%prep
%setup -q -n sk1sdk-%{version}%{subver}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHTS
%dir %{py_sitedir}/sk1sdk
%dir %{py_sitedir}/sk1sdk/libtk
%dir %{py_sitedir}/sk1sdk/libttk
%dir %{py_sitedir}/sk1sdk/tkXcursor
%dir %{py_sitedir}/sk1sdk/tkimage
%dir %{py_sitedir}/sk1sdk/tkpng
%dir %{py_sitedir}/sk1sdk/tkstyle

%{py_sitedir}/sk1sdk/*.py[co]
%{py_sitedir}/sk1sdk/libtk/*.py[co]
%{py_sitedir}/sk1sdk/libttk/*.py[co]
%{py_sitedir}/sk1sdk/tkXcursor/*.py[co]
%{py_sitedir}/sk1sdk/tkimage/*.py[co]
%{py_sitedir}/sk1sdk/tkpng/*.py[co]
%{py_sitedir}/sk1sdk/tkpng/*.tcl
%{py_sitedir}/sk1sdk/tkstyle/*.py[co]
%{py_sitedir}/sk1sdk/tkstyle/colors
%{py_sitedir}/sk1sdk/tkstyle/icons
%{py_sitedir}/sk1sdk/tkstyle/themes
%{py_sitedir}/sk1sdk-%{version}%{subver}-py*.egg-info

%attr(755,root,root) %{py_sitedir}/sk1sdk/libtk/_tkinter.so
%attr(755,root,root) %{py_sitedir}/sk1sdk/tkXcursor/_tkXcursor.so
%attr(755,root,root) %{py_sitedir}/sk1sdk/tkimage/_imagingtk.so
%attr(755,root,root) %{py_sitedir}/sk1sdk/tkpng/libtkpng.so

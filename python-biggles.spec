%include        /usr/lib/rpm/macros.python

Summary:	high-level scientific plotting module for Python
Name:		python-biggles
Version:	1.6.3
Release:	0.1
Source0:	http://dl.sourceforge.net/biggles/%{name}-%{version}.tar.gz
# Source0-md5:	316717ce5f54311d47853e6b2948a329
URL:		http://biggles.sourceforge.net/
License:	GPL
Group:		Applications/Graphics
BuildRequires:	libplot-devel
BuildRequires:	python-numpy-devel
Requires:	plotutils
Requires:	python >= 1.5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define bigglesdir %{_libdir}/lib/python1.5/site-packages/biggles

%description
Biggles is a Python module for creating publication-quality 2D
scientific plots. It supports multiple output formats (postscript,
x11, png, svg, gif), understands simple TeX, and sports a high-level,
elegant interface. It's intended for technical users with
sophisticated plotting needs.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{bigglesdir}/libplot
install src/config.ini $RPM_BUILD_ROOT%{bigglesdir}/config.ini
install src/*.{py{,c},so}  $RPM_BUILD_ROOT%{bigglesdir}/
install src/libplot/*.{py{,c},so}  $RPM_BUILD_ROOT%{bigglesdir}/libplot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING CREDITS ChangeLog README examples
%dir %{bigglesdir}
%config %{bigglesdir}/config.ini
%{bigglesdir}/*.py
%{bigglesdir}/*.pyc
%attr(755,root,root) %{bigglesdir}/*.so
%dir %{bigglesdir}/libplot
%{bigglesdir}/libplot/*.py
%{bigglesdir}/libplot/*.pyc
%attr(755,root,root) %{bigglesdir}/libplot/*.so

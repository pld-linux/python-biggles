
#
# todo:
# - remove *.py
#

%define		filename	python2-biggles
Summary:	High-level scientific plotting module for Python
Summary(pl):	Wysokopoziomowy modu³ do wykresów naukowych dla Pythona
Name:		python-biggles
Version:	1.6.4
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/biggles/%{filename}-%{version}.tar.gz
# Source0-md5:	e07bc9e22d830ada274ea71bc6d12556
Patch0:		%{name}-configdir.patch
URL:		http://biggles.sourceforge.net/
BuildRequires:	libplot-devel
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel
BuildRequires:	rpm-pythonprov
Requires:	plotutils
Requires:	python >= 1.5.2
Requires:	python-numpy
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		bigglesdir	%{py_sitedir}/biggles

%description
Biggles is a Python module for creating publication-quality 2D
scientific plots. It supports multiple output formats (PostScript,
X11, PNG, SVG, GIF), understands simple TeX, and supports a
high-level, elegant interface. It's intended for technical users with
sophisticated plotting needs.

%description -l pl
Biggles to modu³ Pythona do tworzenia wykresów naukowych 2D z jako¶ci±
wystarczaj±c± dla publikacji. Obs³uguje wiele formatów wyj¶ciowych
(PostScript, X11, PNG, SVG, GIF), rozumie prostego TeXa i obs³uguje
wysokopoziomowy, elegancki interfejs. Jest przeznaczony dla
u¿ytkowników technicznych z wyszukanymi wymaganiami co do wykresów.

%prep
%setup -q -n %{filename}-%{version}
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -ansi -Wall" \
	LDFLAGS="-L%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{bigglesdir}/libplot

install -D src/config.ini $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/config.ini
install src/*.{py{,c},so} $RPM_BUILD_ROOT%{bigglesdir}
install src/libplot/*.{py{,c},so} $RPM_BUILD_ROOT%{bigglesdir}/libplot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README examples
%dir %{bigglesdir}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/config.ini
%{bigglesdir}/*.py
%{bigglesdir}/*.pyc
%attr(755,root,root) %{bigglesdir}/*.so
%dir %{bigglesdir}/libplot
%{bigglesdir}/libplot/*.py
%{bigglesdir}/libplot/*.pyc
%attr(755,root,root) %{bigglesdir}/libplot/*.so

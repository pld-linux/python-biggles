
#
# todo:
# - put config.ini into sysconfdir
# - remove *.py
#

%include        /usr/lib/rpm/macros.python

Summary:	High-level scientific plotting module for Python
Summary(pl):	Wysokopoziomowy modu³ do wykresów naukowych dla Pythona
Name:		python-biggles
Version:	1.6.3
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/biggles/%{name}-%{version}.tar.gz
# Source0-md5:	316717ce5f54311d47853e6b2948a329
URL:		http://biggles.sourceforge.net/
BuildRequires:	libplot-devel
BuildRequires:	python-numpy-devel
BuildRequires:	rpm-pythonprov
Requires:	plotutils
Requires:	python >= 1.5.2
Requires:	python-numpy
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
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -ansi -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{bigglesdir}/libplot

install src/config.ini $RPM_BUILD_ROOT%{bigglesdir}/config.ini
install src/*.{py{,c},so}  $RPM_BUILD_ROOT%{bigglesdir}
install src/libplot/*.{py{,c},so}  $RPM_BUILD_ROOT%{bigglesdir}/libplot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README examples
%dir %{bigglesdir}
%config %{bigglesdir}/config.ini
%{bigglesdir}/*.py
%{bigglesdir}/*.pyc
%attr(755,root,root) %{bigglesdir}/*.so
%dir %{bigglesdir}/libplot
%{bigglesdir}/libplot/*.py
%{bigglesdir}/libplot/*.pyc
%attr(755,root,root) %{bigglesdir}/libplot/*.so

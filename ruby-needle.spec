%define pkgname needle
Summary:	Dependency injection for Ruby
Summary(pl.UTF-8):	Wprowadzanie zależności dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.3.0
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	53ae8ec8d73fed8aafa6bfc628b032d2
URL:		http://needle.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-Needle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Needle is a dependency injection (also, inversion of control)
container for Ruby.

%description -l pl.UTF-8
Needle to kontener wprowadzający zależności (a także odwrócenie
sterowania) dla języka Ruby.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

rm ri/*.rid

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*
%{ruby_ridir}/*

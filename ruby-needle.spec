Summary:	Dependency injection for Ruby
Summary(pl):	Wprowadzanie zale¿no¶ci dla jêzyka Ruby
Name:		ruby-Needle
Version:	1.2.0
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/1931/needle-%{version}.tar.bz2
# Source0-md5:	44ca6c4037c93667318acd376203f092
URL:		http://needle.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-modules
Requires:	ruby-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Needle is a dependency injection (also, inversion of control)
container for Ruby.

%description -l pl
Needle to kontener wprowadzaj±cy zale¿no¶ci (a tak¿e odwrócenie
sterowania) dla jêzyka Ruby.

%prep
%setup -q -n needle-%{version}

%build
ruby setup.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*
%{ruby_ridir}/*

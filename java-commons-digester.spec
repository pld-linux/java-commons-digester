Summary:	Jakarta Commons Digester
Name:		jakarta-commons-digester
Version:	1.3
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-commons/release/commons-digester/v1.3/commons-digester-1.3-src.tar.gz
URL:		http://jakarta.apache.org/
Requires:	jre
BuildRequires:	jakarta-ant
BuildRequires:	jakarta-commons-logging
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Jakarta Commons Digester.

%package doc
Summary:	Jakarta Commons Digester
Group:		Development/Languages/Java

%description doc
Jakarta Commons Digester.

%prep
%setup -q -n commons-digester-%{version}-src

%build
touch LICENSE
cd digester
ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install digester/dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc digester/LICENSE.txt
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc digester/dist/docs

Summary:	Jakarta Commons Digester - XML to Java object mapping
Summary(pl):	Jakarta Commons Digester - odwzorowanie XML na obiekty Javy
Name:		jakarta-commons-digester
Version:	1.3
Release:	2
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-commons/release/commons-digester/v%{version}/commons-digester-%{version}-src.tar.gz
# Source0-md5:	0dafb55a57c4bd3b2a941d2961b139c8
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant
BuildRequires:	jakarta-commons-beanutils
BuildRequires:	jakarta-commons-collections
BuildRequires:	jakarta-commons-logging
BuildRequires:	jdk >= 1.2
Requires:	jre >= 1.2
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-collections
Requires:	jakarta-commons-logging
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
This scope of the Digester component is primarily oriented to XML ->
Java object mapping.

A Digester processes an XML input stream by matching a series of
element nesting patterns to execute Rules that have been added prior
to the start of parsing. This package was inspired by the XmlMapper
class that was part of Tomcat 3.0 and 3.1, but is organized somewhat
differently.

%description -l pl
Zakresem dzia³ania komponentu Digester jest zorientowany g³ównie na
odwzorowywanie XML na obiekty Javy.

Digester przetwarza strumieñ wej¶ciowy XML dopasowuj±c serie wzorców
zagnie¿d¿ania elementów, aby wykonywaæ regu³y dodane przed
rozpoczêciem analizy. Ten pakiet by³ zainspirowany klas± XmlMapper,
która by³a czê¶ci± Tomcata 3.0 i 3.1, ale jest zorganizowany nieco
inaczej.

%package doc
Summary:	Jakarta Commons Digester documentation
Summary(pl):	Dokumentacja do Jakarta Commons Digester
Group:		Development/Languages/Java

%description doc
Jakarta Commons Digester documentation.

%description doc -l pl
Dokumentacja do Jakarta Commons Digester.

%prep
%setup -q -n commons-digester-%{version}-src

%build
cat << EOF > build.properties
commons-beanutils.jar=%{_javalibdir}/commons-beanutils.jar
commons-collections.jar=%{_javalibdir}/commons-collections.jar
commons-logging.jar=%{_javalibdir}/commons-logging.jar
EOF
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

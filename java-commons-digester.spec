Summary:	Jakarta Commons Digester - XML to Java object mapping
Summary(pl):	Jakarta Commons Digester - odwzorowanie XML-a na obiekty Javy
Name:		jakarta-commons-digester
Version:	1.5
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://apache.org/dist/jakarta/commons/digester/source/commons-digester-%{version}-src.tar.gz
# Source0-md5:	f678cc07c41c37b6ac4e63fe972f8364
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

%description
This scope of the Digester component is primarily oriented to XML ->
Java object mapping.

A Digester processes an XML input stream by matching a series of
element nesting patterns to execute Rules that have been added prior
to the start of parsing. This package was inspired by the XmlMapper
class that was part of Tomcat 3.0 and 3.1, but is organized somewhat
differently.

%description -l pl
Zakresem dzia�ania komponentu Digester jest zorientowany g��wnie na
odwzorowywanie XML-a na obiekty Javy.

Digester przetwarza strumie� wej�ciowy XML dopasowuj�c serie wzorc�w
zagnie�d�ania element�w, aby wykonywa� regu�y dodane przed
rozpocz�ciem analizy. Ten pakiet by� zainspirowany klas� XmlMapper,
kt�ra by�a cz�ci� Tomcata 3.0 i 3.1, ale jest zorganizowany nieco
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
commons-beanutils.jar=%{_javadir}/commons-beanutils.jar
commons-collections.jar=%{_javadir}/commons-collections.jar
commons-logging.jar=%{_javadir}/commons-logging.jar
EOF
touch LICENSE
ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs

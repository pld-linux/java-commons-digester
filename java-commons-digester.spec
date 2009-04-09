#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
%bcond_with     java_sun        # build with java-sun

%if "%{pld_release}" == "ti"
%bcond_without	java_sun	# build with gcj
%else
%bcond_with	java_sun	# build with java-sun
%endif

%include	/usr/lib/rpm/macros.java

%define		srcname commmons-digester
Summary:	Commons Digester - XML to Java object mapping
Summary(pl.UTF-8):	Commons Digester - odwzorowanie XML-a na obiekty Javy
Name:		java-commons-digester
Version:	1.7
Release:	3
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/commons/digester/source/%{srcname}-%{version}-src.tar.gz
# Source0-md5:	718f91f6958da865826bca455f644076
URL:		http://commons.apache.org/digester/
BuildRequires:	ant
BuildRequires:	java-commons-beanutils
BuildRequires:	java-commons-collections
BuildRequires:	java-commons-logging
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java-commons-beanutils
Requires:	java-commons-collections
Requires:	java-commons-logging
Requires:	jpackage-utils
Provides:	jakarta-commons-digester
Obsoletes:	jakarta-commons-digester
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

%description -l pl.UTF-8
Zakresem działania komponentu Digester jest zorientowany głównie na
odwzorowywanie XML-a na obiekty Javy.

Digester przetwarza strumień wejściowy XML dopasowując serie wzorców
zagnieżdżania elementów, aby wykonywać reguły dodane przed
rozpoczęciem analizy. Ten pakiet był zainspirowany klasą XmlMapper,
która była częścią Tomcata 3.0 i 3.1, ale jest zorganizowany nieco
inaczej.

%package javadoc
Summary:	Commons Digester documentation
Summary(pl.UTF-8):	Dokumentacja do Commons Digester
Group:		Documentation
Provides:	jakarta-commons-digester-javadoc
Obsoletes:	jakarta-commons-digester-doc
Obsoletes:	jakarta-commons-digester-javadoc

%description javadoc
Commons Digester documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Commons Digester.

%prep
%setup -q -n %{srcname}-%{version}-src

%build
required_jars="commons-beanutils-core commons-collections commons-logging"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH

%ant clean dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a dist/%{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a dist/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc RELEASE-NOTES.txt
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif

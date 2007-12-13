%include	/usr/lib/rpm/macros.java
Summary:	Jakarta Commons Digester - XML to Java object mapping
Summary(pl.UTF-8):	Jakarta Commons Digester - odwzorowanie XML-a na obiekty Javy
Name:		jakarta-commons-digester
Version:	1.7
Release:	2
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/digester/source/commons-digester-%{version}-src.tar.gz
# Source0-md5:	718f91f6958da865826bca455f644076
URL:		http://jakarta.apache.org/commons/digester/
BuildRequires:	ant
BuildRequires:	jakarta-commons-beanutils
BuildRequires:	jakarta-commons-collections
BuildRequires:	jakarta-commons-logging
BuildRequires:	jdk >= 1.2
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-collections
Requires:	jakarta-commons-logging
Requires:	jpackage-utils
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
Summary:	Jakarta Commons Digester documentation
Summary(pl.UTF-8):	Dokumentacja do Jakarta Commons Digester
Group:		Documentation
Obsoletes:	jakarta-commons-digester-doc

%description javadoc
Jakarta Commons Digester documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Jakarta Commons Digester.

%prep
%setup -q -n commons-digester-%{version}-src

%build
required_jars="commons-beanutils commons-collections commons-logging"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH
%ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a dist/commons-digester.jar $RPM_BUILD_ROOT%{_javadir}/commons-digester-%{version}.jar
ln -s commons-digester-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-digester.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a dist/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc LICENSE.txt RELEASE-NOTES.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

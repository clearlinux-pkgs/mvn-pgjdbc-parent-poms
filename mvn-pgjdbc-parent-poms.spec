#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-pgjdbc-parent-poms
Version  : el1.0.3
Release  : 2
URL      : https://github.com/pgjdbc/pgjdbc-parent-poms/archive/REL1.0.3.tar.gz
Source0  : https://github.com/pgjdbc/pgjdbc-parent-poms/archive/REL1.0.3.tar.gz
Source1  : https://repo1.maven.org/maven2/org/postgresql/pgjdbc-core-parent/1.0.3/pgjdbc-core-parent-1.0.3.pom
Source2  : https://repo1.maven.org/maven2/org/postgresql/pgjdbc-core-prevjre/1.0.3/pgjdbc-core-prevjre-1.0.3.pom
Source3  : https://repo1.maven.org/maven2/org/postgresql/pgjdbc-versions/1.0.3/pgjdbc-versions-1.0.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-pgjdbc-parent-poms-data = %{version}-%{release}

%description
<img src="http://developer.postgresql.org/~josh/graphics/logos/elephant-64.png" />
# Parent poms for PostgreSQL JDBC driver

%package data
Summary: data components for the mvn-pgjdbc-parent-poms package.
Group: Data

%description data
data components for the mvn-pgjdbc-parent-poms package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/postgresql/pgjdbc-core-parent/1.0.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/postgresql/pgjdbc-core-parent/1.0.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/postgresql/pgjdbc-core-prevjre/1.0.3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/postgresql/pgjdbc-core-prevjre/1.0.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/postgresql/pgjdbc-versions/1.0.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/postgresql/pgjdbc-versions/1.0.3


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/postgresql/pgjdbc-core-parent/1.0.3/pgjdbc-core-parent-1.0.3.pom
/usr/share/java/.m2/repository/org/postgresql/pgjdbc-core-prevjre/1.0.3/pgjdbc-core-prevjre-1.0.3.pom
/usr/share/java/.m2/repository/org/postgresql/pgjdbc-versions/1.0.3/pgjdbc-versions-1.0.3.pom

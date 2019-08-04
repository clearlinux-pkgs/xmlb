#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xmlb
Version  : 0.1.11
Release  : 2
URL      : https://github.com/hughsie/libxmlb/archive/0.1.11/libxmlb-0.1.11.tar.gz
Source0  : https://github.com/hughsie/libxmlb/archive/0.1.11/libxmlb-0.1.11.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: xmlb-data = %{version}-%{release}
Requires: xmlb-lib = %{version}-%{release}
Requires: xmlb-libexec = %{version}-%{release}
Requires: xmlb-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : glib-dev
BuildRequires : gobject-introspection
BuildRequires : gtk-doc
BuildRequires : libxslt
BuildRequires : pkgconfig(gio-2.0)

%description
libxmlb
=======
Introduction
------------
XML is slow to parse and strings inside the document cannot be memory mapped as
they do not have a trailing NUL char. The libxmlb library takes XML source, and
converts it to a structured binary representation with a deduplicated string
table -- where the strings have the NULs included.

%package data
Summary: data components for the xmlb package.
Group: Data

%description data
data components for the xmlb package.


%package dev
Summary: dev components for the xmlb package.
Group: Development
Requires: xmlb-lib = %{version}-%{release}
Requires: xmlb-data = %{version}-%{release}
Provides: xmlb-devel = %{version}-%{release}
Requires: xmlb = %{version}-%{release}

%description dev
dev components for the xmlb package.


%package doc
Summary: doc components for the xmlb package.
Group: Documentation

%description doc
doc components for the xmlb package.


%package lib
Summary: lib components for the xmlb package.
Group: Libraries
Requires: xmlb-data = %{version}-%{release}
Requires: xmlb-libexec = %{version}-%{release}
Requires: xmlb-license = %{version}-%{release}

%description lib
lib components for the xmlb package.


%package libexec
Summary: libexec components for the xmlb package.
Group: Default
Requires: xmlb-license = %{version}-%{release}

%description libexec
libexec components for the xmlb package.


%package license
Summary: license components for the xmlb package.
Group: Default

%description license
license components for the xmlb package.


%prep
%setup -q -n libxmlb-0.1.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564945807
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/xmlb
cp LICENSE %{buildroot}/usr/share/package-licenses/xmlb/LICENSE
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Xmlb-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/installed-tests/libxmlb/libxmlb.test
/usr/share/installed-tests/libxmlb/test.xml.gz.gz.gz

%files dev
%defattr(-,root,root,-)
/usr/include/libxmlb-1/libxmlb/xb-builder-fixup.h
/usr/include/libxmlb-1/libxmlb/xb-builder-node.h
/usr/include/libxmlb-1/libxmlb/xb-builder-source-ctx.h
/usr/include/libxmlb-1/libxmlb/xb-builder-source.h
/usr/include/libxmlb-1/libxmlb/xb-builder.h
/usr/include/libxmlb-1/libxmlb/xb-machine.h
/usr/include/libxmlb-1/libxmlb/xb-node-query.h
/usr/include/libxmlb-1/libxmlb/xb-node.h
/usr/include/libxmlb-1/libxmlb/xb-opcode.h
/usr/include/libxmlb-1/libxmlb/xb-query.h
/usr/include/libxmlb-1/libxmlb/xb-silo-export.h
/usr/include/libxmlb-1/libxmlb/xb-silo-query.h
/usr/include/libxmlb-1/libxmlb/xb-silo.h
/usr/include/libxmlb-1/libxmlb/xb-stack.h
/usr/include/libxmlb-1/libxmlb/xb-string.h
/usr/include/libxmlb-1/libxmlb/xb-version.h
/usr/include/libxmlb-1/xmlb.h
/usr/lib64/libxmlb.so
/usr/lib64/pkgconfig/xmlb.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libxmlb/annotation-glossary.html
/usr/share/gtk-doc/html/libxmlb/api-index-full.html
/usr/share/gtk-doc/html/libxmlb/deprecated-api-index.html
/usr/share/gtk-doc/html/libxmlb/home.png
/usr/share/gtk-doc/html/libxmlb/index.html
/usr/share/gtk-doc/html/libxmlb/intro.html
/usr/share/gtk-doc/html/libxmlb/left-insensitive.png
/usr/share/gtk-doc/html/libxmlb/left.png
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbBuilder.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbBuilderFixup.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbBuilderNode.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbBuilderSource.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbMachine.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbNode.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbQuery.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbSilo.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-node-query.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-opcode.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-silo-query.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-stack.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-string.html
/usr/share/gtk-doc/html/libxmlb/libxmlb.devhelp2
/usr/share/gtk-doc/html/libxmlb/libxmlb.html
/usr/share/gtk-doc/html/libxmlb/right-insensitive.png
/usr/share/gtk-doc/html/libxmlb/right.png
/usr/share/gtk-doc/html/libxmlb/style.css
/usr/share/gtk-doc/html/libxmlb/up-insensitive.png
/usr/share/gtk-doc/html/libxmlb/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxmlb.so.1
/usr/lib64/libxmlb.so.1.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/xb-self-test
/usr/libexec/xb-tool

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xmlb/LICENSE
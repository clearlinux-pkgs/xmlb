#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : xmlb
Version  : 0.3.14
Release  : 20
URL      : https://github.com/hughsie/libxmlb/archive/0.3.14/libxmlb-0.3.14.tar.gz
Source0  : https://github.com/hughsie/libxmlb/archive/0.3.14/libxmlb-0.3.14.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: xmlb-bin = %{version}-%{release}
Requires: xmlb-data = %{version}-%{release}
Requires: xmlb-lib = %{version}-%{release}
Requires: xmlb-license = %{version}-%{release}
Requires: xmlb-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : libxslt
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libzstd)
BuildRequires : xz-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libxmlb
=======
Introduction
------------
XML is slow to parse and strings inside the document cannot be memory mapped as
they do not have a trailing NUL char. The libxmlb library takes XML source, and
converts it to a structured binary representation with a deduplicated string
table -- where the strings have the NULs included.

%package bin
Summary: bin components for the xmlb package.
Group: Binaries
Requires: xmlb-data = %{version}-%{release}
Requires: xmlb-license = %{version}-%{release}

%description bin
bin components for the xmlb package.


%package data
Summary: data components for the xmlb package.
Group: Data

%description data
data components for the xmlb package.


%package dev
Summary: dev components for the xmlb package.
Group: Development
Requires: xmlb-lib = %{version}-%{release}
Requires: xmlb-bin = %{version}-%{release}
Requires: xmlb-data = %{version}-%{release}
Provides: xmlb-devel = %{version}-%{release}
Requires: xmlb = %{version}-%{release}

%description dev
dev components for the xmlb package.


%package doc
Summary: doc components for the xmlb package.
Group: Documentation
Requires: xmlb-man = %{version}-%{release}

%description doc
doc components for the xmlb package.


%package lib
Summary: lib components for the xmlb package.
Group: Libraries
Requires: xmlb-data = %{version}-%{release}
Requires: xmlb-license = %{version}-%{release}

%description lib
lib components for the xmlb package.


%package license
Summary: license components for the xmlb package.
Group: Default

%description license
license components for the xmlb package.


%package man
Summary: man components for the xmlb package.
Group: Default

%description man
man components for the xmlb package.


%package tests
Summary: tests components for the xmlb package.
Group: Default
Requires: xmlb = %{version}-%{release}

%description tests
tests components for the xmlb package.


%prep
%setup -q -n libxmlb-0.3.14
cd %{_builddir}/libxmlb-0.3.14
pushd ..
cp -a libxmlb-0.3.14 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692983282
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/xmlb
cp %{_builddir}/libxmlb-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/xmlb/b386b371ce94933e63ced1052aa72a60da5485ff || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xb-tool
/usr/bin/xb-tool

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Xmlb-2.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libxmlb-2/libxmlb/xb-builder-fixup.h
/usr/include/libxmlb-2/libxmlb/xb-builder-node.h
/usr/include/libxmlb-2/libxmlb/xb-builder-source-ctx.h
/usr/include/libxmlb-2/libxmlb/xb-builder-source.h
/usr/include/libxmlb-2/libxmlb/xb-builder.h
/usr/include/libxmlb-2/libxmlb/xb-machine.h
/usr/include/libxmlb-2/libxmlb/xb-node-query.h
/usr/include/libxmlb-2/libxmlb/xb-node-silo.h
/usr/include/libxmlb-2/libxmlb/xb-node.h
/usr/include/libxmlb-2/libxmlb/xb-opcode.h
/usr/include/libxmlb-2/libxmlb/xb-query-context.h
/usr/include/libxmlb-2/libxmlb/xb-query.h
/usr/include/libxmlb-2/libxmlb/xb-silo-export.h
/usr/include/libxmlb-2/libxmlb/xb-silo-query.h
/usr/include/libxmlb-2/libxmlb/xb-silo.h
/usr/include/libxmlb-2/libxmlb/xb-stack.h
/usr/include/libxmlb-2/libxmlb/xb-string.h
/usr/include/libxmlb-2/libxmlb/xb-value-bindings.h
/usr/include/libxmlb-2/libxmlb/xb-version.h
/usr/include/libxmlb-2/xmlb.h
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
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbBuilderSourceCtx.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbMachine.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbNode.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbQuery.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-XbSilo.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-node-query.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-opcode.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-query-context.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-silo-export.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-silo-query.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-stack.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-string.html
/usr/share/gtk-doc/html/libxmlb/libxmlb-xb-value-bindings.html
/usr/share/gtk-doc/html/libxmlb/libxmlb.devhelp2
/usr/share/gtk-doc/html/libxmlb/libxmlb.html
/usr/share/gtk-doc/html/libxmlb/right-insensitive.png
/usr/share/gtk-doc/html/libxmlb/right.png
/usr/share/gtk-doc/html/libxmlb/style.css
/usr/share/gtk-doc/html/libxmlb/up-insensitive.png
/usr/share/gtk-doc/html/libxmlb/up.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libxmlb.so.2.0.0
/usr/lib64/libxmlb.so.2
/usr/lib64/libxmlb.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xmlb/b386b371ce94933e63ced1052aa72a60da5485ff

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xb-tool.1

%files tests
%defattr(-,root,root,-)
/V3/usr/libexec/installed-tests/libxmlb/xb-self-test
/usr/libexec/installed-tests/libxmlb/test.desktop
/usr/libexec/installed-tests/libxmlb/test.quirk
/usr/libexec/installed-tests/libxmlb/test.xml
/usr/libexec/installed-tests/libxmlb/test.xml.gz.gz.gz
/usr/libexec/installed-tests/libxmlb/test.xml.xz
/usr/libexec/installed-tests/libxmlb/test.xml.zstd
/usr/libexec/installed-tests/libxmlb/xb-self-test
/usr/share/installed-tests/libxmlb/libxmlb.test

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v16
# autospec commit: b858a2a
#
Name     : appstream-glib
Version  : 0.8.3
Release  : 22
URL      : https://people.freedesktop.org/~hughsient/appstream-glib/releases/appstream-glib-0.8.3.tar.xz
Source0  : https://people.freedesktop.org/~hughsient/appstream-glib/releases/appstream-glib-0.8.3.tar.xz
Summary  : Objects and helper methods to help reading and writing AppStream metadata
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: appstream-glib-bin = %{version}-%{release}
Requires: appstream-glib-data = %{version}-%{release}
Requires: appstream-glib-lib = %{version}-%{release}
Requires: appstream-glib-license = %{version}-%{release}
Requires: appstream-glib-locales = %{version}-%{release}
Requires: appstream-glib-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : curl-dev
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gperf
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libgcab-1.0)
BuildRequires : pkgconfig(uuid)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
| ⚠️ WARNING: appstream-glib is heavy maintenance mode, use [appstream](https://github.com/ximion/appstream) instead |
| --- |

%package bin
Summary: bin components for the appstream-glib package.
Group: Binaries
Requires: appstream-glib-data = %{version}-%{release}
Requires: appstream-glib-license = %{version}-%{release}

%description bin
bin components for the appstream-glib package.


%package data
Summary: data components for the appstream-glib package.
Group: Data

%description data
data components for the appstream-glib package.


%package dev
Summary: dev components for the appstream-glib package.
Group: Development
Requires: appstream-glib-lib = %{version}-%{release}
Requires: appstream-glib-bin = %{version}-%{release}
Requires: appstream-glib-data = %{version}-%{release}
Provides: appstream-glib-devel = %{version}-%{release}
Requires: appstream-glib = %{version}-%{release}

%description dev
dev components for the appstream-glib package.


%package lib
Summary: lib components for the appstream-glib package.
Group: Libraries
Requires: appstream-glib-data = %{version}-%{release}
Requires: appstream-glib-license = %{version}-%{release}

%description lib
lib components for the appstream-glib package.


%package license
Summary: license components for the appstream-glib package.
Group: Default

%description license
license components for the appstream-glib package.


%package locales
Summary: locales components for the appstream-glib package.
Group: Default

%description locales
locales components for the appstream-glib package.


%package man
Summary: man components for the appstream-glib package.
Group: Default

%description man
man components for the appstream-glib package.


%package tests
Summary: tests components for the appstream-glib package.
Group: Default
Requires: appstream-glib = %{version}-%{release}

%description tests
tests components for the appstream-glib package.


%prep
%setup -q -n appstream-glib-0.8.3
cd %{_builddir}/appstream-glib-0.8.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721086823
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddep11=false \
-Drpm=false  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/appstream-glib
cp %{_builddir}/appstream-glib-%{version}/COPYING %{buildroot}/usr/share/package-licenses/appstream-glib/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/appstream-glib-%{version}/data/tests/rpmbuild-font/COPYING %{buildroot}/usr/share/package-licenses/appstream-glib/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang appstream-glib

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/appstream-builder
/usr/bin/appstream-compose
/usr/bin/appstream-util

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/AppStreamGlib-1.0.typelib
/usr/share/bash-completion/completions/appstream-builder
/usr/share/bash-completion/completions/appstream-util
/usr/share/gettext/its/appdata.its
/usr/share/gettext/its/appdata.loc
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libappstream-glib/appstream-glib.h
/usr/include/libappstream-glib/as-agreement-section.h
/usr/include/libappstream-glib/as-agreement.h
/usr/include/libappstream-glib/as-app-builder.h
/usr/include/libappstream-glib/as-app.h
/usr/include/libappstream-glib/as-bundle.h
/usr/include/libappstream-glib/as-checksum.h
/usr/include/libappstream-glib/as-content-rating.h
/usr/include/libappstream-glib/as-enums.h
/usr/include/libappstream-glib/as-format.h
/usr/include/libappstream-glib/as-icon.h
/usr/include/libappstream-glib/as-image.h
/usr/include/libappstream-glib/as-inf.h
/usr/include/libappstream-glib/as-launchable.h
/usr/include/libappstream-glib/as-markup.h
/usr/include/libappstream-glib/as-monitor.h
/usr/include/libappstream-glib/as-node.h
/usr/include/libappstream-glib/as-problem.h
/usr/include/libappstream-glib/as-profile.h
/usr/include/libappstream-glib/as-provide.h
/usr/include/libappstream-glib/as-release.h
/usr/include/libappstream-glib/as-require.h
/usr/include/libappstream-glib/as-review.h
/usr/include/libappstream-glib/as-screenshot.h
/usr/include/libappstream-glib/as-store.h
/usr/include/libappstream-glib/as-suggest.h
/usr/include/libappstream-glib/as-tag.h
/usr/include/libappstream-glib/as-translation.h
/usr/include/libappstream-glib/as-utils.h
/usr/include/libappstream-glib/as-version.h
/usr/lib64/libappstream-glib.so
/usr/lib64/pkgconfig/appstream-glib.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/asb-plugins-5/libasb_plugin_appdata.so
/usr/lib64/asb-plugins-5/libasb_plugin_desktop.so
/usr/lib64/asb-plugins-5/libasb_plugin_font.so
/usr/lib64/asb-plugins-5/libasb_plugin_gettext.so
/usr/lib64/asb-plugins-5/libasb_plugin_hardcoded.so
/usr/lib64/asb-plugins-5/libasb_plugin_icon.so
/usr/lib64/asb-plugins-5/libasb_plugin_shell_extension.so
/usr/lib64/libappstream-glib.so.8
/usr/lib64/libappstream-glib.so.8.0.10

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/appstream-glib/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/appstream-glib/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/appstream-builder.1
/usr/share/man/man1/appstream-compose.1
/usr/share/man/man1/appstream-util.1

%files tests
%defattr(-,root,root,-)
/usr/share/installed-tests/appstream-glib/appdata-validate.test
/usr/share/installed-tests/appstream-glib/destdir-check.test

%files locales -f appstream-glib.lang
%defattr(-,root,root,-)


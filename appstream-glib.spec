#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : appstream-glib
Version  : 0.7.4
Release  : 2
URL      : https://people.freedesktop.org/~hughsient/appstream-glib/releases/appstream-glib-0.7.4.tar.xz
Source0  : https://people.freedesktop.org/~hughsient/appstream-glib/releases/appstream-glib-0.7.4.tar.xz
Summary  : Test package
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1
Requires: appstream-glib-bin
Requires: appstream-glib-lib
Requires: appstream-glib-data
Requires: appstream-glib-locales
Requires: appstream-glib-doc
BuildRequires : docbook-xml
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gperf
BuildRequires : libxslt-bin
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libgcab-1.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(uuid)
BuildRequires : python3

%description
This is a test font.

%package bin
Summary: bin components for the appstream-glib package.
Group: Binaries
Requires: appstream-glib-data

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
Requires: appstream-glib-lib
Requires: appstream-glib-bin
Requires: appstream-glib-data
Provides: appstream-glib-devel

%description dev
dev components for the appstream-glib package.


%package doc
Summary: doc components for the appstream-glib package.
Group: Documentation

%description doc
doc components for the appstream-glib package.


%package lib
Summary: lib components for the appstream-glib package.
Group: Libraries
Requires: appstream-glib-data

%description lib
lib components for the appstream-glib package.


%package locales
Summary: locales components for the appstream-glib package.
Group: Default

%description locales
locales components for the appstream-glib package.


%prep
%setup -q -n appstream-glib-0.7.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512157305
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Denable-rpm=false -Denable-dep11=false -Denable-stemmer=false builddir
ninja -v -C builddir

%install
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
/usr/lib64/girepository-1.0/AppStreamBuilder-1.0.typelib
/usr/lib64/girepository-1.0/AppStreamGlib-1.0.typelib
/usr/share/bash-completion/completions/appstream-builder
/usr/share/bash-completion/completions/appstream-util
/usr/share/gettext/its/appdata.its
/usr/share/gettext/its/appdata.loc
/usr/share/gir-1.0/*.gir
/usr/share/installed-tests/appstream-glib/appdata-validate.test
/usr/share/installed-tests/appstream-glib/destdir-check.test

%files dev
%defattr(-,root,root,-)
/usr/include/libappstream-builder/appstream-builder.h
/usr/include/libappstream-builder/asb-app.h
/usr/include/libappstream-glib/appstream-glib.h
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
/usr/lib64/libappstream-builder.so
/usr/lib64/libappstream-glib.so
/usr/lib64/pkgconfig/appstream-builder.pc
/usr/lib64/pkgconfig/appstream-glib.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/asb-plugins-5/libasb_plugin_appdata.so
/usr/lib64/asb-plugins-5/libasb_plugin_desktop.so
/usr/lib64/asb-plugins-5/libasb_plugin_font.so
/usr/lib64/asb-plugins-5/libasb_plugin_gettext.so
/usr/lib64/asb-plugins-5/libasb_plugin_hardcoded.so
/usr/lib64/asb-plugins-5/libasb_plugin_shell_extension.so
/usr/lib64/libappstream-builder.so.8
/usr/lib64/libappstream-builder.so.8.0.10
/usr/lib64/libappstream-glib.so.8
/usr/lib64/libappstream-glib.so.8.0.10

%files locales -f appstream-glib.lang
%defattr(-,root,root,-)

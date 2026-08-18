Name:           snixembed
Version:        0.1.0
Release:        1%{?dist}
Summary:        Proxy StatusNotifierItems as XEmbedded system tray icons

License:        MIT
URL:            https://git.sr.ht/~steef/snixembed
Source0:        https://git.sr.ht/~steef/snixembed/archive/%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  pkgconfig
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  libdbusmenu-devel
BuildRequires:  libdbusmenu-gtk3-devel

Requires:       gtk3
Requires:       glib2
Requires:       libdbusmenu-gtk3

%description
snixembed acts as a proxy between the StatusNotifierItem (SNI) and the older
XEmbed-based system tray icon protocols. It presents itself as a
StatusNotifierHost on the D-Bus session bus and uses GTK+3 to maintain
corresponding XEmbed tray icons.

%prep
%autosetup -n snixembed-%{version}

# Upstream generates version.vala from Git metadata and therefore expects
# .git/HEAD to exist. Release tarballs don't contain .git, so provide the
# release version ourselves and remove the Git dependency from the Makefile.
sed -i 's/\.git\/HEAD//' Makefile

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/snixembed
%{_mandir}/man1/snixembed.1*

%changelog
* Tue Aug 18 2026 Zac aRRAY <your-email@example.com> - 0.1.0-1
- Initial package

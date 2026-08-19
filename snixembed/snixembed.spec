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

# Generate a deterministic version file for release-tarball builds.
cat > version.vala <<'EOF'
const string VERSION = "%{version}";
EOF

# Prevent make from regenerating version.vala from Git metadata.
sed -i 's/^version\.vala:.*$/version.vala:/' makefile

%build
%make_build

%install
%make_install PREFIX=%{_prefix} BINDIR=%{_bindir} MANDIR=%{_mandir}

%files
%license LICENSE
%doc README.md
%{_bindir}/snixembed
%{_mandir}/man1/snixembed.1*

%changelog
* Tue Aug 18 2026 Zac aRRAY <your-email@example.com> - 0.1.0-1
- Initial package

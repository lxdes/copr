Name:           snixembed
Version:        0.3.3
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

cat > version.vala <<'EOF'
const string VERSION = "%{version}";
EOF
sed -i 's/^version\.vala:.*$/version.vala:/' makefile

cat > %{name}-autostart.desktop <<'EOF'
[Desktop Entry]
Version=1.0
Type=Application
NoDisplay=false
Name=snixembed
GenericName=StatusNotifierItems to X tray
Comment=Proxy StatusNotifierItems as XEmbedded systemtray-spec icons
Keywords=StatusNotifierItems;tray
TryExec=snixembed
Exec=snixembed
StartupNotify=false
Terminal=false
EOF

%build
%make_build

%install
%make_install PREFIX=%{_prefix} BINDIR=%{_bindir} MANDIR=%{_mandir}
install -Dm644 %{name}-autostart.desktop \
    %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/snixembed
%{_mandir}/man1/snixembed.1*
%{_sysconfdir}/xdg/autostart/%{name}.desktop

%changelog
* Tue Aug 18 2026 Zac <your-email@example.com> - 0.3.3-1
- Update to 0.3.3
- Add optional XDG autostart entry

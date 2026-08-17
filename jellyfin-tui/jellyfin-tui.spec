%global crate jellyfin-tui
%global debug_package %{nil}

Name:           %{crate}
Version:        1.5.2
Release:        1%{?dist}
Summary:        Music streaming TUI client for Jellyfin
License:        GPL-3.0-only
URL:            https://github.com/dhonus/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
AutoReq:        off

Requires:       mpv

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  openssl-devel

%description
A feature-rich, music streaming Terminal User Interface (TUI) client for Jellyfin.

%prep
%autosetup -n %{crate}-%{version}

%build
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1

cargo build --release

%install
install -Dm0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm0644 LICENSE %{buildroot}%{_licensedir}/%{name}
install -Dm0644 src/extra/jellyfin-tui.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license %{_licensedir}/%{name}
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Aug 18 2026 - 1.5.2-1
- Update to version 1.5.2
- Use refs/tags for Source0 URL
- Add debug_package %{nil}
- Remove unnecessary runtime dependencies

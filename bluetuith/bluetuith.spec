%global crate bluetuith
%global debug_package %{nil}

Name:           %{crate}
Version:        0.2.7
Release:        1%{?dist}
Summary:        A TUI bluetooth manager for Linux
License:        MIT
URL:            https://github.com/bluetuith-org/%{name}
Source0:        https://github.com/bluetuith-org/%{name}/releases/download/v%{version}/%{name}_%{version}_Linux_x86_64.tar.gz
Requires:       bluez

%description
bluetuith is a TUI-based Bluetooth manager for Linux with a terminal interface.

%prep
%setup -q

%build

%install
install -Dm0755 %{crate} %{buildroot}%{_bindir}/%{crate}
install -Dm0644 LICENSE %{buildroot}%{_licensedir}/%{crate}/LICENSE

%files
%license %{_licensedir}/%{crate}/LICENSE
%{_bindir}/%{crate}

%changelog
* Wed Aug 20 2026 - 0.2.7-1
- Update to version 0.2.7

* Mon Aug 18 2025 - 0.2.5-1
- Initial COPR packaging from binary release

%global debug_package %{nil}

Name:           betterlockscreen
Version:        4.4.0
Release:        1%{?dist}
Summary:        Fast lockscreen for Linux systems with effects
License:        MIT
URL:            https://github.com/betterlockscreen/%{name}
Source0:       https://github.com/betterlockscreen/%{name}/archive/refs/tags/v%{version}.tar.gz
%global _sonaming %{version}

Requires:       i3lock-color
Requires:       ImageMagick
Requires:       xorg-x11-utils
Requires:       xorg-x11-server-X11
Requires:       xorg-x11-server-utils
Requires:       bash

BuildRequires:  bash

%description
Betterlockscreen is a fast and visually appealing lockscreen wrapper for Linux
systems. It takes an image or directory, applies various effects (blur, dim,
pixelate, color), caches the results, and uses i3lock-color for locking. The
cached images provide a natural lockscreen experience without the typical
2-3 second delay.

%prep
%autosetup -n %{name}-%{version}

%build

%install
# Main script
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

# Systemd service file
install -Dm0644 system/%{name}@.service \
    %{buildroot}%{_unitdir}/%{name}@.service

# Example configuration
install -Dm0644 examples/%{name}rc \
    %{buildroot}%{_docdir}/%{name}/%{name}rc

%pre
useradd --no-user-group --system --shell /bin/false --comment "Betterlockscreen service account" "%{name}" || true

%files
%license LICENSE
%doc README.md examples/
%{_bindir}/%{name}
%{_unitdir}/%{name}@.service

%changelog
* Wed Aug 20 2026 - 4.4.0-1
- Initial package

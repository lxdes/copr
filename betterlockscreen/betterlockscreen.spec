Name: betterlockscreen
Version: 4.4.0
Release: 1%{?dist}
Summary: Sweet looking lockscreen wrapper for i3lock-color

License: MIT
URL: https://github.com/betterlockscreen/betterlockscreen
Source0: https://github.com/betterlockscreen/betterlockscreen/archive/refs/tags/v%{version}.tar.gz

BuildArch: noarch
BuildRequires: systemd-rpm-macros

Requires: bash
Requires: bc
Requires: feh
Requires: i3lock-color
Requires: ImageMagick
Requires: xdpyinfo
Requires: xrandr

%description
betterlockscreen is a bash script that uses i3lock-color to lock your
screen with dynamic visual effects and custom background images.

%prep
%autosetup -n %{name}-%{version}

%install
install -Dpm 0755 betterlockscreen -t %{buildroot}%{_bindir}/
install -Dpm 0644 system/betterlockscreen@.service -t %{buildroot}%{_unitdir}/
install -Dpm 0644 examples/betterlockscreenrc -t %{buildroot}%{_pkgdocdir}/examples/

%files
%license LICENSE
%doc README.md
%{_bindir}/betterlockscreen
%{_unitdir}/betterlockscreen@.service
%{_pkgdocdir}/examples/betterlockscreenrc

%changelog
* Mon Aug 17 2026 lxde 4.4.0-1
- Updated to version 4.4.0
- Fixed metadata summary and description
- Fixed macro paths and license declaration

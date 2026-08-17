%global debug_package %{nil}

# betterlockscreen package
%global bls_version 4.4.0
%global bls_release 1

# i3lock-color package
%global i3lock_version 2.13.c.5
%global i3lock_release 1

Name:           betterlockscreen
Version:        %{bls_version}
Release:        %{bls_release}%{?dist}
Summary:        Fast lockscreen for Linux systems with effects
License:        MIT
URL:            https://github.com/betterlockscreen/%{name}
Source0:        https://github.com/betterlockscreen/%{name}/archive/refs/tags/v%{bls_version}.tar.gz
Source1:        https://github.com/Raymo111/i3lock-color/archive/refs/tags/%{i3lock_version}.tar.gz

Requires:       i3lock-color
Requires:       ImageMagick
Requires:       xorg-x11-utils
Requires:       xorg-x11-server-X11
Requires:       xorg-x11-server-utils
Requires:       bash

BuildRequires:  bash
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jpeg)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(ev)
BuildRequires:  pam-devel
BuildRequires:  libev-devel
BuildRequires:  libX11-devel
BuildRequires:  libx11-xcb-devel

%description
Betterlockscreen is a fast and visually appealing lockscreen wrapper for Linux
systems. It takes an image or directory, applies various effects (blur, dim,
pixelate, color), caches the results, and uses i3lock-color for locking.

%package -n i3lock-color
Summary:        Improved version of the original i3lock screen locker
License:        BSD-3-Clause AND MIT

%description -n i3lock-color
i3lock-color is an improved version of the original i3lock screen locker. It
features support for background images, improved color selection, and other
visual enhancements.

%prep
%autosetup -n betterlockscreen-%{bls_version}
# Unpack i3lock-color alongside betterlockscreen sources
tar -xf %{SOURCE1}

%build
# i3lock-color: build with autotools
pushd i3lock-color-%{i3lock_version}
autoreconf -fi
%configure --with-libinput
%make_build
popd

%install
# betterlockscreen: install main script
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

# betterlockscreen: systemd service file
install -Dm0644 system/%{name}@.service \
    %{buildroot}%{_unitdir}/%{name}@.service

# betterlockscreen: example configuration
install -Dm0644 examples/%{name}rc \
    %{buildroot}%{_docdir}/%{name}/%{name}rc

# i3lock-color: install binary
install -Dm0755 i3lock-color-%{i3lock_version}/i3lock \
    %{buildroot}%{_bindir}/i3lock-color

# i3lock-color: install man page
install -Dm0644 i3lock-color-%{i3lock_version}/i3lock.1 \
    %{buildroot}%{_mandir}/man1/i3lock-color.1

%files
%license LICENSE
%doc README.md examples/
%{_bindir}/%{name}
%{_unitdir}/%{name}@.service
%{_docdir}/%{name}/%{name}rc

%files -n i3lock-color
%{_bindir}/i3lock-color
%{_mandir}/man1/i3lock-color.1*

%changelog
* Mon Aug 17 2026 Packaging Maintainer <maintainer@example.com> - 4.4.0-1
- Initial package with i3lock-color subpackage

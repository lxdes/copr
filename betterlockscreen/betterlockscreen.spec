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
BuildRequires:  pkg-config
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
BuildRequires:  libx11-xcb-devel
BuildRequires:  libxcb-xkb-devel
BuildRequires:  libxcb-xinerama-devel
BuildRequires:  libxcb-randr-devel
BuildRequires:  libxcb-composite-devel
BuildRequires:  libxcb-image-devel
BuildRequires:  libxcb-util-devel
BuildRequires:  libxcb-xrm-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libjpeg-devel
BuildRequires:  fontconfig-devel
BuildRequires:  cairo-devel

%package i3lock-color
Summary:        Improved version of the original i3lock screen locker
License:        ISC
URL:            https://github.com/Raymo111/i3lock-color

%description
Betterlockscreen is a fast and visually appealing lockscreen wrapper for Linux
systems. It takes an image or directory, applies various effects (blur, dim,
pixelate, color), caches the results, and uses i3lock-color for locking. The
cached images provide a natural lockscreen experience without the typical
2-3 second delay.

%description i3lock-color
i3lock-color is an improved version of the original i3lock screen locker. It
features support for background images, improved color selection, and other
visual enhancements.

%prep
%autosetup -n betterlockscreen-%{bls_version}
%setup -q -a1 -n i3lock-color-%{i3lock_version}

%build
# i3lock-color: build with autotools
%pushd i3lock-color-%{i3lock_version}
autoreconf -fi
%configure --with-libinput
make %{?_smp_mflags}
%popd

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
install -Dm0755 i3lock-color-%{i3lock_version}/build/i3lock \
    %{buildroot}%{_bindir}/i3lock-color

# i3lock-color: install man page
install -Dm0644 i3lock-color-%{i3lock_version}/build/i3lock.1 \
    %{buildroot}%{_mandir}/man1/i3lock.1

# i3lock-color: install completion scripts
install -Dm0644 i3lock-color-%{i3lock_version}/build/bash_completion \
    %{buildroot}%{_datadir}/bash-completion/completions/i3lock
install -Dm0644 i3lock-color-%{i3lock_version}/build/zsh_completion.zsh \
    %{buildroot}%{_datadir}/zsh/site-functions/_i3lock

%pre
useradd --no-user-group --system --shell /bin/false --comment "Betterlockscreen service account" "%{name}" || true

%files
%license betterlockscreen-%{bls_version}/LICENSE
%doc betterlockscreen-%{bls_version}/README.md betterlockscreen-%{bls_version}/examples/
%{_bindir}/%{name}
%{_unitdir}/%{name}@.service

%files i3lock-color
%{_bindir}/i3lock-color
%{_mandir}/man1/i3lock.1*
%{_datadir}/bash-completion/completions/i3lock
%{_datadir}/zsh/site-functions/_i3lock

%changelog
* Mon Aug 17 2026 - 4.4.0-1
- Initial package with i3lock-color dependency

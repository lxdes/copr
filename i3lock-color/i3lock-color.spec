%global _vpath_builddir .

Name: i3lock-color
Version: 2.13.c.5
Release: 1%{?dist}
Summary: The world's most popular non-default computer lockscreen.

License: MIT
URL: https://github.com/Raymo111/i3lock-color
Source0: %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: gcc
BuildRequires: libev-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libX11-devel
BuildRequires: libXinerama-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXrandr-devel
BuildRequires: make
BuildRequires: pam-devel
BuildRequires: pkgconfig
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-xrm-devel

%description
i3lock-color is a fork of i3lock, a simple screen locker. It features
color customization, text positioning, blurred backgrounds, and additional
visual parameters.

%prep
%autosetup -n %{name}-%{version}

%build
autoreconf -fi
%configure \
	--disable-sanitizers \
	--enable-debug=no

%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md CHANGELOG
%{_bindir}/i3lock
%{_mandir}/man1/i3lock.1*
%{_sysconfdir}/pam.d/i3lock

%changelog
* Mon Aug 17 2026 lxde 2.13.c.5-1
- Initial Fedora packaging release for version 2.13.c.5
- Disabled out-of-source build macro to fix make target errors

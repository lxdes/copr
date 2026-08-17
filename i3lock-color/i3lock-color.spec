Name:           i3lock-color
Version:        2.13.c.5
Release:        1%{?dist}
Summary:        Modern fork of i3lock with color features and visual enhancements

License:        MIT
URL:            https://github.com/Raymo111/i3lock-color
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Provides:       i3lock = %{version}
Conflicts:      i3lock

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-xrm-devel

%description
i3lock-color is a fork of i3lock, a simple screen locker. It features
color customization, text positioning, blurred backgrounds, and additional
visual parameters.

%prep
%autosetup -n %{name}-%{version}

%build
autoreconf -fi

./configure \
    --disable-builddir \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir} \
    --mandir=%{_mandir} \
    --disable-sanitizers \
    --enable-debug=no

%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/i3lock
%{_mandir}/man1/i3lock.1*
%config(noreplace) %{_sysconfdir}/pam.d/i3lock

%changelog
* Mon Aug 17 2026 lxde - 2.13.c.5-1
- Initial Fedora packaging release

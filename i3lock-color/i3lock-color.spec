Name:           i3lock-color
Version:        2.13.c.5
Release:        1%{?dist}
Summary:        The world's most popular non-default computer lockscreen.

License: MIT
URL: https://github.com/Raymo111/i3lock-color
Source0: https://github.com/Raymo111/i3lock-color/archive/refs/tags/%{version}.tar.gz

BuildRequires: autoconf automake cairo-devel fontconfig gcc libev-devel pkgconf
BuildRequires: libjpeg-turbo-devel libXinerama libxkbcommon-devel libxkbcommon-x11-devel libXrandr pam-devel xcb-util-image-devel xcb-util-xrm-devel
BuildRequires: git
Requires: bash

%description
i3lock is a simple screen locker like slock. After starting it, you will see a white screen (you can configure the color/an image).
You can return to your screen by entering your password.


%prep
%autosetup

%build
autoreconf -fi
	./configure --prefix="$pkgdir/usr/" \
        --sysconfdir="$pkgdir/etc/" \
        --enable-debug=no \
        --disable-sanitizers

%make_build

%install
%make_install


%files
%{_bindir}/i3lock
%{_mandir}/man1/i3lock.1.*
%{_sysconfdir}/pam.d/i3lock
%doc README.md i3lock.1 CHANGELOG
%license LICENSE

%changelog
* Sat Sep 09 2023 Rubem Mota <rubemmota89@gmail.com>
* Updated to version 2.13.c.5
* Sat Feb 25 2023 Rubem Mota <rubemmota89@gmail.com>
* First release

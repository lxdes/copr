
%global  real_name plasma-workspace
%global  bin_name  xembedsniproxy

Name:    xembed-sni-proxy
Summary: Legacy xembed tray icons support for SNI-only system trays
Version: 6.5.2
Release: 1%{?dist}

License: GPLv2+
URL:     https://github.com/KDE/%{real_name}
Source:  %{url}/archive/v%{version}/%{real_name}-%{version}.tar.gz

# https://aur.archlinux.org/cgit/aur.git/plain/cmake.patch?h=xembed-sni-proxy-git
Patch:   cmake.patch
Patch:   service.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  libXtst-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-image-devel

Conflicts:      %{real_name}
Requires:       dbus

%description
%{summary}.
Standalone package for non-KDE environments.


%prep
%autosetup -p1 -n %{real_name}-%{version}
# enable xdg autostart for non-KDE environments
sed -i -e '/^OnlyShowIn=/d' %{name}/%{bin_name}.desktop
# set version
sed -i -e 's/%%{version}/%{version}/' xembed-sni-proxy/CMakeLists.txt


%build
%global _vpath_srcdir %{name}
%cmake_kf6
%cmake_build


%install
%cmake_install


%check
desktop-file-validate \
    %{buildroot}%{_sysconfdir}/xdg/autostart/%{bin_name}.desktop

%post
%systemd_user_post %{bin_name}.service

%preun
%systemd_user_preun %{bin_name}.service


%files
%{_sysconfdir}/xdg/autostart/%{bin_name}.desktop
%{_bindir}/%{bin_name}
%{_userunitdir}/%{bin_name}.service


%changelog
* Thu Nov 06 2025 Aleksei Bavshin <alebastr@fedoraproject.org> - 6.5.2-1
- Update to 6.5.2

* Sat Nov 11 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 5.27.9.1-1
- Update to 5.27.9.1

* Fri Feb 19 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 5.21.0-1
- Update to 5.21.0

* Wed Mar 18 2020 Aleksei Bavshin <alebastr89@gmail.com> - 5.18.3-1
- Initial packaging (based on AUR package)


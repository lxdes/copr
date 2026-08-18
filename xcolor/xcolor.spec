# Non-vendored build — requires network access during %build
%global crate xcolor

Name: xcolor
Version: 0.5.1
Release: 1%{?dist}
Summary: Lightweight color picker for X11

License: MIT
URL: https://github.com/Soft/xcolor
Source0: %{crates_source}

BuildRequires: cargo-rpm-macros
BuildRequires: pkg-config
BuildRequires: glibc-devel
BuildRequires: libX11-devel
BuildRequires: libXcursor-devel
BuildRequires: libxcb-devel

%description
xcolor is a lightweight, scriptable color picker for X11. It provides a
simple CLI tool to pick colors from screen and output them in various
formats. It uses the Xlib and XCB libraries for screen capture and
cursor information.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep -N
sed -i 's/offline = true/offline = false/' .cargo/config.toml

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%{_bindir}/xcolor

%changelog
* Mon Aug 17 2026 0.5.1-1
- Initial package

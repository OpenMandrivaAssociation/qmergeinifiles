Name: qmergeinifiles
Version: 1.91.0
Release: 1

Summary: Utility to merge INI-format files
Group: Development/Other
License: GPL

Requires: qt4-common

Source: %name-%version.tar

BuildRequires: gcc-c++ libqt4-devel libstdc++-devel

%description
Utility to merge INI-format files

%prep
%setup -q
%qmake_qt4

%build
%make CUSTOM_OPT_FLAGS="%optflags"

%install
%make INSTALL_ROOT=%buildroot install


%files
%_bindir/*


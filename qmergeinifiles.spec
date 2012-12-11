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



%changelog
* Thu Jan 12 2012 Александр Казанцев <kazancas@mandriva.org> 1.91.0-1
+ Revision: 760276
- imported package qmergeinifiles


* Thu Jan 12 2012 Alexander Kazancev <kazancas@mandriva.org> 1.91.0-mdv1
- import to Mandriva

* Thu Oct 27 2011 Sergey V Turchin <zerg@altlinux.org> 1.91.0-alt1
- create General section only if exists according settings

* Wed Oct 26 2011 Sergey V Turchin <zerg@altlinux.org> 1.90.0-alt1
- rewrite to merge without recoding text

* Tue Jan 26 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- fix compile with new Qt

* Fri Nov 09 2007 Sergey V Turchin <zerg at altlinux dot org> 0.0.1-alt1
- initial specfile


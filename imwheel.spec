%global pkgrel      1.0.0
%global extraver    pre12

Name:           imwheel
Version:        %{pkgrel}
Release:        0.1.%{extraver}%{?dist}
Summary:        Mouse Event to Key Event Mapper Daemon

License:        GPLv2+
Url:            http://imwheel.sourceforge.net
Source:         http://prdownloads.sourceforge.net/imwheel/imwheel-%{pkgrel}%{extraver}.tar.gz
# PATCH-FIX-UPSTREAM to prevent compiler warnings
# "cast from pointer to integer of different size"
Patch1:         imwheel-intptr_t.patch
# PATCH-FIX-UPSTREAM to fix uninitialized variable hsi.
Patch2:         imwheel-fix_uninitialized_var.patch
# PATCH-FIX-OPENSUSE not to install to root only.
Patch3:         imwheel-fix_destdir.patch
# PATCH-FEATURE-OPENSUSE to put configs to /etc/ instead of /etc/X11.
Patch4:         imwheel-config_file_path.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)

%description
A daemon for X11, which watches for mouse wheel actions and outputs them as
keypresses. It can be configured separately for different windows. It also
allows input from it's own (included) gpm, or from jamd, or from XFree86 ZAxis
mouse wheel conversion.

%prep
%autosetup -p0 -n %{name}-%{pkgrel}%{extraver}

%build
autoreconf -fiv
%configure \
  --with-x 
%make_build

%install
%make_install

%files
%doc AUTHORS BUGS ChangeLog EMACS FREEBSD
%doc M-BA47 NEWS README TODO
%license COPYING
%config(noreplace) %{_sysconfdir}/imwheelrc
%{_bindir}/imwheel
%{_mandir}/man1/imwheel.1*

%changelog
* Tue Aug 29 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.0-0.1.pre12
- Correct spec for fedora

* Tue Jul 14 2015 mpluskal@suse.com
- Clenaup spec file with spec-cleaner
- Include %%changelog in spec file
- Trim dependencies
* Mon Apr 22 2013 cfarrell@suse.com
- license update: GPL-2.0+
  No indication in package that GPL-2.0 (i.e. "only") is intended
* Sat Apr 20 2013 dap.darkness@gmail.com
- Macro replacing "makeinstall" => "make_install"
  via `spec-cleaner` was reverted to build at SLE_11_SP2.
* Sat Apr  6 2013 dap.darkness@gmail.com
- Spec header and changes file were added to correspond to distro policy.
- License tag was set to GPL-2.0 to correspond to distro policy.
- Spec file was fixed up via `spec-cleaner`.
- Patches were commented to correspond to distro policy.
- Clean section was removed as unnecessary.

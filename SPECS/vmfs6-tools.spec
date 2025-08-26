#
# spec file for package vmfs6-tools
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           vmfs6-tools
Version:        0.2.1
Release:        lp160.1.6.1%{?dist}
Summary:        Tools to access VMFS6 filesystems
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/teward/vmfs6-tools
#Git-Clone:     https://github.com/weafon/vmfs6-tool.git
# This is the same releasetarball debian ia using ...
Source:         https://github.com/teward/vmfs6-tools/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         vmfs-tools-uuid
BuildRequires:  asciidoc
BuildRequires:  docbook-style-xsl
BuildRequires:  libuuid-devel
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
# XCP-ng
BuildRequires:  gcc

%define ext_man .gz

%description
Originally loosely based on the vmfs code from fluidOps, this set of tools has
since evolved to handle more features from VMFS, such as extents, and allows to
access VMFS through the standard Linux VFS with the help of the FUSE framework.

The code in the project is only for VMFS6 for now since the format of VMFS6
changed significantly.

While it is still work in progress and is not destined for production use yet,
it can be of some help for some people.

%package -n libvmfs6-devel
Summary:        Library to access VMFS filesystems
Group:          Development/Libraries/C and C++
Requires:       libuuid-devel

%description -n libvmfs6-devel
Originally loosely based on the vmfs code from fluidOps, this set of tools has
since evolved to handle more features from VMFS, such as extents, and allows to
access VMFS through the standard Linux VFS with the help of the FUSE framework.

The code in the project is only for VMFS6 for now since the format of VMFS6
changed significantly.

While it is still work in progress and is not destined for production use yet,
it can be of some help for some people.

%prep
%setup -q
%patch -P 1 -p1

%build
%configure
%make_build

%install
%make_install
install -d "%{buildroot}%{_includedir}/libvmfs6"
install -m0644 libvmfs/*.h "%{buildroot}%{_includedir}/libvmfs6/"

%files
%license LICENSE
%doc README
%{_sbindir}/debugvmfs6
%{_sbindir}/fsck.vmfs6
%{_sbindir}/vmfs6-fuse
%{_sbindir}/vmfs6-lvm
%{_mandir}/man8/debugvmfs6.8%{?ext_man}
%{_mandir}/man8/fsck.vmfs6.8%{?ext_man}
%{_mandir}/man8/vmfs6-fuse.8%{?ext_man}
%{_mandir}/man8/vmfs6-lvm.8%{?ext_man}

%files -n libvmfs6-devel
%{_includedir}/libvmfs6

%changelog
* Tue Aug 26 2025 Yann Dirson <yann.dirson@vates.tech> - 0.2.1-lp160.1.6.1
- Import from OpenSuSE and build for XCP-ng 8.3
- Adjust package name for Docbook XSL styleshets
- Adjust ext_man macro to find gzipped manpages
- Add gcc in breqs so it builds in our koji

* Thu Aug 29 2024 Martin Hauke <mardnh@gmx.de>
- Initial package on obs for vmfs6-tools
  based on filesystems/vmfs-tools
* Sat Sep 26 2015 mpluskal@suse.com
- Cleanup spec file with spec-clener
- Cleanup dependencies
- Do not install static libraries
- Remove conditionals for old releases
* Fri Feb 27 2015 Greg.Freemyer@gmail.com
- update to version 0.2.5
  * limited VMFS 5 support (Seems limited to 255 GB or smaller files)
  * experimental extent removal
  * some deep changes to the debugvmfs tool
  * various fixes
- use pkgconfig(fuse) instead of fuse-devel for BuildRequires
* Sat May 26 2012 jengelh@inai.de
- Remove redundant tags/sections from specfile
* Mon May  7 2012 jeffm@suse.com
- Build fixes for libuuid-devel
* Wed Mar 23 2011 pascal.bleser@opensuse.org
- initial version (0.2.1)

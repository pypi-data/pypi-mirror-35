#!/usr/bin/env python3
# -*- encoding: utf-8 -*-






RPM_SPEC = '''
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Summary: __PKG_SUMMARY__
Name: __PKG_NAME__
Version: __PKG_VERSION__
Release: __PKG_RELEASE__
License: __PKG_LICENSE__
Group: __PKG_GROUP__
Source: %{name}-%{version}.tar.gz
AutoReq: no
__PKG_REQUIRES__
URL: __PKG_URL__
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
__PKG_RELOCATIONS__

%description
__PKG_DESCRIPTION__

%prep
%setup -q

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}

# in builddir
if [ -e usr/bin ]
then
    mkdir -p %{buildroot}/usr/bin
    cp -a usr/bin/* %{buildroot}/usr/bin
fi

if [ -e usr/sbin ]
then
    mkdir -p %{buildroot}/usr/sbin
    cp -a usr/sbin/* %{buildroot}/usr/sbin
fi

if [ -e usr/lib ]
then
    mkdir -p %{buildroot}/usr/lib

    # Ignore error if nothing matches
    cp -a usr/lib/lib*.so* %{buildroot}/usr/lib || true
fi

if [ -e usr/lib/systemd/system/ ]
then
    mkdir -p %{buildroot}/usr/lib/systemd/system

    # Ignore error if nothing matches
    cp -a usr/lib/systemd/system/*.service %{buildroot}/usr/lib/systemd/system || true
fi

if [ -e usr/share ]
then
    mkdir -p %{buildroot}/usr/share
    cp -dr usr/share/* %{buildroot}/usr/share
fi

if [ -e usr/local ]
then
    mkdir -p %{buildroot}/usr/local
    cp -dr usr/local/* %{buildroot}/usr/local
fi

if [ -e etc ]
then
    mkdir -p %{buildroot}/etc
    cp -dr etc/* %{buildroot}/etc
fi

if [ -e var ]
then
    mkdir -p %{buildroot}/var
    cp -dr var/* %{buildroot}/var
fi

if [ -e opt ]
then
    mkdir -p %{buildroot}/opt
    cp -dr opt/* %{buildroot}/opt
fi

# Only post, preun and postun if any systemd service.
%if 0%{?rpm_systemd_services:1}

# See https://fedoraproject.org/wiki/Packaging:Scriptlets for the order and
# conditions.

# On upgrade only (before new install and old uninstall)
%pre
    if [ "$1" -eq 2 ]
    then
        systemctl disable --now %rpm_systemd_services
    fi

# On uninstall only, not on upgrade
%preun
    if [ "$1" -eq 0 ]
    then
        systemctl disable --now %rpm_systemd_services
    fi

%postun
    systemctl daemon-reload

# After new install and old uninstall
%posttrans
    echo "posttrans: $1"
    systemctl daemon-reload
    systemctl enable --now %rpm_systemd_services

%endif # End of rpm_sytemd_services


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/

__PKG_CONFIG_ETC__

'''

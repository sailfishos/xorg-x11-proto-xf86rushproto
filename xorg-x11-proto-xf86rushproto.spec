# 
# Do not Edit! Generated by:
# spectacle version 0.13~pre
# 
# >> macros
# << macros

Name:       xorg-x11-proto-xf86rushproto
Summary:    X.Org X11 Protocol xf86rushproto
Version:    1.1.2
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/xf86rushproto-%{version}.tar.bz2
Source100:  xorg-x11-proto-xf86rushproto.yaml
Provides:   xf86rushproto

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Description: %{summary}



%prep
%setup -q -n xf86rushproto-%{version}
# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --libdir=%{_datadir}

# Call make instruction with smp support
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
# >> files
%{_datadir}/pkgconfig/xf86rushproto.pc
%{_includedir}/X11/extensions/xf86rushstr.h
%{_includedir}/X11/extensions/xf86rush.h
# << files



%global gitdate 20180404
%global gitversion 4.2.3
%global gitcommit 5ebc7fe

%global debug_package %{nil}

Name:           cppzmq
Version:        %{gitversion}
Release:        1.git%{gitdate}.%{gitcommit}%{?dist}
Summary:        C++ binding for 0MQ

License:        MIT
URL:            https://github.com/zeromq/cppzmq
Source0:        cppzmq.tar.bz2
Patch0:         cppzmq-fix-project-version.patch
Patch1:         cppzmq-disable-tests.patch

BuildRequires:  cmake >= 3.0.0
BuildRequires:  zeromq-devel >= %{gitversion}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       zeromq-devel%{?_isa} >= %{gitversion}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n cppzmq
%patch0 -p1
%patch1 -p1


%build
mkdir Build
pushd Build
%{cmake} \
    -DCPPZMQ_CMAKECONFIG_INSTALL_DIR=%{_libdir}/cmake/cppzmq \
    ..
make %{?_smp_mflags}
popd


%install
rm -rf $RPM_BUILD_ROOT
pushd Build
%make_install
popd


%files devel
%license LICENSE
%doc README.md
%{_includedir}/*
%{_libdir}/cmake/cppzmq


%changelog
* Wed Apr 04 2018 Jajauma's Packages <jajauma@yandex.ru> - 4.2.3-1.git20180404.5ebc7fe
- Initial packaging

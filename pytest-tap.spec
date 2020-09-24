#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-tap
Version  : 3.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/c5/75/9ccc2cf1c698d32cb8b35c13219c5f0cc54bfc2edcb429ba1b3a0807c28c/pytest-tap-3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/75/9ccc2cf1c698d32cb8b35c13219c5f0cc54bfc2edcb429ba1b3a0807c28c/pytest-tap-3.1.tar.gz
Summary  : Test Anything Protocol (TAP) reporting plugin for pytest
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pytest-tap-license = %{version}-%{release}
Requires: pytest-tap-python = %{version}-%{release}
Requires: pytest-tap-python3 = %{version}-%{release}
Requires: pytest
BuildRequires : buildreq-distutils3
BuildRequires : pytest

%description
pytest-tap
==========
|version| |license| |travis| |travismac| |appveyor| |coverage|

%package license
Summary: license components for the pytest-tap package.
Group: Default

%description license
license components for the pytest-tap package.


%package python
Summary: python components for the pytest-tap package.
Group: Default
Requires: pytest-tap-python3 = %{version}-%{release}

%description python
python components for the pytest-tap package.


%package python3
Summary: python3 components for the pytest-tap package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_tap)
Requires: pypi(tap.py)
Requires: pypi(pytest)

%description python3
python3 components for the pytest-tap package.


%prep
%setup -q -n pytest-tap-3.1
cd %{_builddir}/pytest-tap-3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587497629
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-tap
cp %{_builddir}/pytest-tap-3.1/LICENSE %{buildroot}/usr/share/package-licenses/pytest-tap/2af827e8d0e30e38b0fa186a2e75c51abec9c46f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-tap/2af827e8d0e30e38b0fa186a2e75c51abec9c46f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

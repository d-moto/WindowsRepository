Summary: A custom command to check the current CPU usage, CPU core, Memory usage.
Name: getsysinfo
Version: 1.0
Release: 1
License: MIT
Source0: getsysinfo.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package provides the getsysinfo command, which checks the current CPU usage, CPU cores, Memory usage, and outputs a message and exit status.

%prep
cp %{_sourcedir}/../getsysinfo.c %{_builddir}/
cp %{_sourcedir}/../getsysinfo.c %{_sourcedir}/

%build
gcc -o getsysinfo %{_builddir}/getsysinfo.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 %{_builddir}/getsysinfo $RPM_BUILD_ROOT/usr/bin

%files
%defattr(-,root,root)
/usr/bin/getsysinfo

%changelog
# ここに変更履歴を追加


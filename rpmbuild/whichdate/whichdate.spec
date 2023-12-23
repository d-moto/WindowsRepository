Summary: A custom command to check the current time
Name: whichdate
Version: 1.0
Release: 1
License: MIT
Source0: whichdate.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package provides the whichdate command, which checks the current time and outputs a message and exit status based on the seconds.

%prep
cp %{_sourcedir}/../whichdate.c %{_builddir}/
cp %{_sourcedir}/../whichdate.c %{_sourcedir}/

%build
gcc -o whichdate %{_builddir}/whichdate.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 %{_builddir}/whichdate $RPM_BUILD_ROOT/usr/bin

%files
%defattr(-,root,root)
/usr/bin/whichdate

%changelog
# ここに変更履歴を追加


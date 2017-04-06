Name:          swift-CIProto
Version:       %{__version}
Release:       %{!?__release:1}%{?__release}%{?dist}
Summary:       Modulemap for libiprotocluster

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/my-mail-ru/%{name}
Source0:       https://github.com/my-mail-ru/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: swift-packaging >= 0.6
Provides:      swiftpm(%{url}.git) = %{version}
Requires:      libiprotocluster-devel

%define debug_package %{nil}

%description
Modulemap for libiprotocluster.

%{?__revision:Built from revision %{__revision}.}


%prep
%setup -q


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{swift_clangmoduleroot}/CIProto/
cp module.modulemap *.h %{buildroot}%{swift_clangmoduleroot}/CIProto/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{swift_clangmoduleroot}/CIProto

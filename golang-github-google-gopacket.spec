%global goipath         github.com/google/gopacket
Version:        1.1.15

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        This library provides packet decoding capabilities for Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  libpcap-devel

BuildRequires:  golang(github.com/mdlayher/raw)
BuildRequires:  golang(golang.org/x/net/bpf)
BuildRequires:  golang(golang.org/x/sys/unix)

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup


%install
%goinstall


%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Nov 30 2018 mskalick@redhat.com - 1.1.15-1
- Use version and fix issues from package review

* Mon Nov 26 2018 mskalick@redhat.com - 0-0.1.20181126gitec90f6c
- First package for Fedora


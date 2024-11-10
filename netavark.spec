%undefine _debugsource_packages

Name: netavark
Version: 1.13.0
Release: 1
Source0: https://github.com/containers/netavark/archive/refs/tags/v%{version}.tar.gz
Source1: vendor.tar.xz
Summary: Container network stack
URL: https://github.com/containers/netavark
License: Apache-2.0
Group: Servers
BuildRequires: golang
BuildRequires: go-md2man
BuildRequires: rust
BuildRequires: protobuf-compiler

%description
Netavark is a rust based network stack for containers. It is being designed to
work with Podman but is also applicable for other OCI container management
applications.

%prep
%autosetup -p1 -a 1
mkdir .cargo
cat >>.cargo/config.toml <<'EOF'

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF


%build
%make_build PREFIX=%{_prefix}
%make_build PREFIX=%{_prefix} -C docs

%install
%make_install PREFIX=%{_prefix}

%files
%{_prefix}/lib/systemd/system/netavark-dhcp-proxy.service
%{_prefix}/lib/systemd/system/netavark-dhcp-proxy.socket
%{_prefix}/lib/systemd/system/netavark-firewalld-reload.service
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/netavark
%{_mandir}/man1/netavark.1*

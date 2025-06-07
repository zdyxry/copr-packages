%global debug_package %{nil}

# 仅支持 x86_64 架构，因为上游只提供该架构的预编译二进制文件
ExclusiveArch:  x86_64

Name:           easytier
Version:        2.3.1
Release:        1%{?dist}
Summary:        A simple, secure and scalable overlay network solution

License:        Apache-2.0
URL:            https://github.com/EasyTier/EasyTier
Source0:        https://github.com/EasyTier/EasyTier/releases/download/v%{version}/easytier-linux-x86_64-v%{version}.zip

BuildRequires:  unzip
# 需要 systemd 来安装服务文件
BuildRequires:  systemd-rpm-macros

# 运行时依赖
Requires:       systemd

%description
EasyTier is a simple, secure and scalable overlay network solution, written in Rust.

Key features:
- Decentralized: No need for a central server, nodes can join the network directly
- Cross-platform: Supports Linux, Windows, macOS, FreeBSD, and Android
- High performance: Utilizes modern network protocols and technologies
- Easy to use: Configuration and management can be done via CLI or Web interface
- Secure: Built-in encryption to ensure data transmission security
- NAT traversal: Supports connection establishment behind firewalls and NAT
- Subnet proxy: Allows accessing entire subnets through EasyTier nodes

%prep
%setup -q -c -n %{name}-%{version}

%build
# 不需要构建，使用预编译的二进制文件

%install
# 创建必要的目录
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/easytier
mkdir -p %{buildroot}%{_localstatedir}/log/easytier

# 安装二进制文件（从子目录中）
install -m 755 easytier-linux-x86_64/easytier-core %{buildroot}%{_bindir}/
install -m 755 easytier-linux-x86_64/easytier-cli %{buildroot}%{_bindir}/
install -m 755 easytier-linux-x86_64/easytier-web %{buildroot}%{_bindir}/
install -m 755 easytier-linux-x86_64/easytier-web-embed %{buildroot}%{_bindir}/

# 创建 systemd 服务文件
cat > %{buildroot}%{_unitdir}/easytier.service << 'EOF'
[Unit]
Description=EasyTier Network Service
After=network.target

[Service]
Type=simple
User=root
ExecStart=%{_bindir}/easytier-core --config-file %{_sysconfdir}/easytier/config.toml
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

# 创建默认配置文件
cat > %{buildroot}%{_sysconfdir}/easytier/config.toml << 'EOF'
listeners = [
    "tcp://0.0.0.0:11010",
    "udp://0.0.0.0:11010",
    "wg://0.0.0.0:11011",
    "ws://0.0.0.0:11011/",
    "wss://0.0.0.0:11012/",
]
rpc_portal = "0.0.0.0:0"

[network_identity]
network_name = "default"
network_secret = ""

[flags]

EOF

%post
%systemd_post easytier.service

%preun
%systemd_preun easytier.service

%postun
%systemd_postun_with_restart easytier.service

%files
%{_bindir}/easytier-core
%{_bindir}/easytier-cli
%{_bindir}/easytier-web
%{_bindir}/easytier-web-embed
%{_unitdir}/easytier.service
%config(noreplace) %{_sysconfdir}/easytier/config.toml
%dir %{_sysconfdir}/easytier
%dir %{_localstatedir}/log/easytier

%changelog
* Fri Jun 07 2024 zdyxry <zdyxry@gmail.com> - 2.3.1-1
- Initial RPM package for EasyTier 2.3.1

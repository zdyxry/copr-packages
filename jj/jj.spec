%global debug_package %{nil}

Name:           jj
Version:        0.39.0
Release:        1%{?dist}
Summary:        A Git-compatible VCS that is both simple and powerful

License:        Apache-2.0
URL:            https://github.com/jj-vcs/jj
ExclusiveArch:  x86_64 aarch64
Source0:        https://github.com/jj-vcs/jj/releases/download/v%{version}/jj-v%{version}-x86_64-unknown-linux-musl.tar.gz
Source1:        https://github.com/jj-vcs/jj/releases/download/v%{version}/jj-v%{version}-aarch64-unknown-linux-musl.tar.gz

BuildRequires:  tar
BuildRequires:  gzip

%description
Jujutsu (jj) is a version control system that combines features from Git and
Mercurial, providing a powerful yet user-friendly experience.

Key features:
- Git-compatible: Works with existing Git repositories
- Powerful conflict resolution: Resolve conflicts later, not immediately
- Automatic rebase: Keeps your commits organized automatically
- Undo functionality: Easily undo any operation
- Multiple working copies: Work on different branches simultaneously
- Simple CLI: Intuitive commands that are easy to remember

%prep
%ifarch x86_64
%setup -q -T -a 0 -c %{name}-%{version}
%endif
%ifarch aarch64
%setup -q -T -a 1 -c %{name}-%{version}
%endif

%build
# 不需要构建，使用预编译的二进制文件

%install
# 创建必要的目录
mkdir -p %{buildroot}%{_bindir}

# 安装二进制文件
install -m 755 jj %{buildroot}%{_bindir}/

%files
%{_bindir}/jj

%changelog
* Mon Mar 17 2025 zdyxry <zdyxry@gmail.com> - 0.39.0-1
- Initial RPM package for jj 0.39.0

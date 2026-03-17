# jj COPR Build Notes

## 项目信息
- **名称**: jj (Jujutsu)
- **上游**: https://github.com/jj-vcs/jj
- **描述**: 一个与 Git 兼容的分布式版本控制系统

## 构建说明

本包使用上游发布的预编译二进制文件构建，支持以下架构：
- x86_64
- aarch64

## 更新版本

1. 访问 https://github.com/jj-vcs/jj/releases 查看最新版本
2. 修改 `jj.spec` 中的 `Version:` 字段
3. 更新 `changelog` 部分
4. 测试构建

## 本地测试构建

```bash
cd jj
spectool -g jj.spec
rpmbuild -ba jj.spec
```

## 注意事项

- 使用 musl 静态链接的二进制文件，无额外运行时依赖
- 二进制文件直接来自上游 GitHub Releases

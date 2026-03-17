#!/bin/bash
# Build script for jj COPR

cd "$(dirname "$0")" || exit 1

# 确保 spec 文件语法正确
rpmlint jj.spec

# 下载源代码
spectool -g jj.spec

# 构建 SRPM
rpmbuild -bs --define "_sourcedir $(pwd)" --define "_srcrpmdir $(pwd)" jj.spec

README.md file for the holbertonschool-higher_level_programming
Last login: Tue Mar  4 15:06:15 on ttys000
-bash: bash_env: command not found

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
MacBook-Pro-de-Laamri-10:~ laamrisaid$ brew install mysql
==> Auto-updating Homebrew...
Adjust how often this is run with HOMEBREW_AUTO_UPDATE_SECS or disable with
HOMEBREW_NO_AUTO_UPDATE. Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
largetifftools             ov                         semver
==> New Casks
consul

Warning: You are using macOS 10.15.
We (and Apple) do not provide support for this old version.
It is expected behaviour that some formulae will fail to build in this old version.
It is expected behaviour that Homebrew will be buggy and slow.
Do not create any issues about this on Homebrew's GitHub repositories.
Do not create any issues even if you think this message is unrelated.
Any opened issues will be immediately closed without response.
Do not ask for help from Homebrew or its maintainers on social media.
You may ask for help in Homebrew's discussions but are unlikely to receive a response.
Try to figure out the problem yourself and submit a fix as a pull request.
We will review it but may or may not accept it.

==> Fetching dependencies for mysql: llvm
==> Fetching llvm
==> Downloading https://raw.githubusercontent.com/Homebrew/homebrew-core/178a101
######################################################################### 100.0%
==> Downloading https://github.com/llvm/llvm-project/commit/1682c99a8877364f1d84
Already downloaded: /Users/laamrisaid/Library/Caches/Homebrew/downloads/35c3ebf4f3d066d306d66806d66db7a90aa021d1000e76dd78eb164e3a4d447c--1682c99a8877364f1d847395cef501e813804caa.patch
==> Downloading https://github.com/llvm/llvm-project/commit/88dd0d33147a7f46a3c9
Already downloaded: /Users/laamrisaid/Library/Caches/Homebrew/downloads/55523293d1828b002c44f6b262d94ac2368422406176eb4076dae6d7aff604a8--88dd0d33147a7f46a3c9df4aed28ad4e47ef597c.patch
==> Downloading https://github.com/llvm/llvm-project/commit/a3e8b860788934d7cc14
Already downloaded: /Users/laamrisaid/Library/Caches/Homebrew/downloads/bca0b9166fb1f7085c1feac844ad29645fd530142c4f99e674a98e7c4cd46828--a3e8b860788934d7cc1489f850f00dcfd9d8b595.patch
==> Downloading https://github.com/llvm/llvm-project/releases/download/llvmorg-1
Already downloaded: /Users/laamrisaid/Library/Caches/Homebrew/downloads/c37a5fe9b8e5b030d7744a13501f8ab4c9689dc02790efcee78623e28dd21970--llvm-project-19.1.7.src.tar.xz
==> Fetching mysql
==> Downloading https://raw.githubusercontent.com/Homebrew/homebrew-core/178a101
######################################################################### 100.0%
==> Downloading https://cdn.mysql.com/Downloads/MySQL-9.2/mysql-9.2.0.tar.gz
Already downloaded: /Users/laamrisaid/Library/Caches/Homebrew/downloads/0dec99a5b81818093799f7a50d7ca37010534cf1956600f69d60fb3940fd8663--mysql-9.2.0.tar.gz
==> Installing dependencies for mysql: llvm
==> Installing mysql dependency: llvm
==> Patching
==> Applying 1682c99a8877364f1d847395cef501e813804caa.patch
==> Applying 88dd0d33147a7f46a3c9df4aed28ad4e47ef597c.patch
==> Applying a3e8b860788934d7cc1489f850f00dcfd9d8b595.patch
==> cmake -G Ninja .. -DLLVM_ENABLE_PROJECTS=clang;clang-tools-extra;mlir;polly;
==> cmake --build .


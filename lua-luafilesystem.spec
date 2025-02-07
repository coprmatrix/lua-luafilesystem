%define luarocks_pkg_name luafilesystem
%define luarocks_pkg_version 1.8.0-1
%define luarocks_pkg_prefix luafilesystem-1.8.0-1
%define luarocks_pkg_major 1.8.0
%define luarocks_pkg_minor 1

Name: lua-luafilesystem
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: File System Library for the Lua Programming Language
Url: https://github.com/lunarmodules/luafilesystem
License: MIT/X11
Source0: luafilesystem-1.8.0-1.tar.gz
Source1: luafilesystem-1.8.0-1.rockspec
BuildRequires: lua-rpm-macros
Requires(postun): alternatives
Requires(post): alternatives
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true
Requires: %{luadist lua >= 5.1}
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
      LuaFileSystem is a Lua library developed to complement the set of
      functions related to file systems offered by the standard Lua
      distribution. LuaFileSystem offers a portable way to access the
      underlying directory structure and file attributes.
   

%prep
%autosetup -p1 -n %{luarocks_pkg_prefix}
%luarocks_prep

%generate_buildrequires
%{?luarocks_buildrequires_echo}
%if %{with check}
%luarocks_generate_buildrequires -c -b
%else
%luarocks_generate_buildrequires -b 
%endif

%build
%{?luarocks_subpackages_build}
%{!?luarocks_subpackages_build:%luarocks_build}

%install
%{?luarocks_subpackages_install}
%{!?luarocks_subpackages_install:%luarocks_install %{luarocks_pkg_prefix}.*.rock}
%{?lua_generate_file_list}

%check
%if %{with check}
%{?luarocks_check}
%endif

%files %{?lua_files}%{!?lua_files:-f lua_files.list}

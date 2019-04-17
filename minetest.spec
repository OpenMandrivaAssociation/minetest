Summary:	An InfiniMiner/Minecraft inspired game
Name:		minetest
Version:	5.0.1
Release:	1
License:	GPLv2+
Group:		Games/Other
Url:		http://minetest.net
# From github by tag
Source0:	https://github.com/minetest/minetest/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/minetest/minetest_game/archive/%{version}/%{name}_game-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	gmp-devel
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	irrlicht-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(jsoncpp)

%description
One of the first InfiniMiner/Minecraft(/whatever) inspired games (started
October 2010), with a goal of taking the survival multiplayer gameplay
to a slightly different direction.

This game is under development, and as of now, the game does not really
differ from Minecraft except for having a lot less features. Still, playing
is quite fun already, especially for people who have not been able to
experience Minecraft.

%files
%doc doc/*.txt
%{_datadir}/doc/minetest/README.md
%{_datadir}/doc/minetest/minetest.conf.example
%{_bindir}/%{name}
#{_bindir}/%{name}server
%{_datadir}/%{name}
%{_datadir}/metainfo/net.minetest.minetest.appdata.xml
%{_datadir}/applications/net.minetest.minetest.desktop
%{_iconsdir}/hicolor/*/apps/%{name}*
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}server.6*

#----------------------------------------------------------------------------

%prep
%setup -q
# Remove bundled lib. Use lib provide by system. (penguin)
rm -vrf lib/jsoncpp lib/lua lib/gmp

%build
# With default LDFLAGS OpenGL is not properly detected for some reasons
%global ldflags %{nil}
#export CC=gcc
#export CXX=g++

%cmake \
	-DENABLE_GETTEXT:BOOL=ON \
	-DCMAKE_CXX_FLAGS_RELEASE=  \
	-DCMAKE_MODULE_LINKER_FLAGS=  \
	-DENABLE_SYSTEM_GMP:BOOL=ON \
	-DENABLE_SYSTEM_JSONCPP:BOOL=ON

%make_build

%install
%make_install -C build

pushd %{buildroot}%{_datadir}/%{name}/games/
tar -xf %{SOURCE1}
mv %{name}_game-%{version} %{name}_game
popd

# Shows empty spaces with current font, must be re-checked in 0.4.8+
rm %{buildroot}%{_datadir}/%{name}/locale/ru/LC_MESSAGES/minetest.mo


Summary:	An InfiniMiner/Minecraft inspired game
Name:		minetest
Version:	0.4.9
Release:	1
License:	GPLv2+
Group:		Games/Other
Url:		http://celeron.55.lt/minetest/
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}_game-%{version}.tar.gz
Source2:	common-0.4.6.zip
Source3:	build-0.4.6.zip
Source4:	survival-0.4.6.zip
Patch1:		minetest-0.4.6-json.patch
Patch2:		minetest-0.4.6-optflags.patch
BuildRequires:	cmake
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	irrlicht-devel
BuildRequires:	jpeg-devel
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
%{_bindir}/%{name}
%{_bindir}/%{name}server
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}-icon.svg
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}server.6*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
# With default LDFLAGS OpenGL is not properly detected for some reasons
%global ldflags %{nil}

%cmake \
	-DENABLE_GETTEXT:BOOL=ON \
	-DCMAKE_CXX_FLAGS_RELEASE=  \
	-DCMAKE_MODULE_LINKER_FLAGS=  

%make

%install
%makeinstall_std -C build

pushd %{buildroot}%{_datadir}/%{name}/games/
tar -xf %{SOURCE1}
unzip %{SOURCE2}
unzip %{SOURCE3}
unzip %{SOURCE4}
mv %{name}_game-%{version} %{name}_game
mv common-0.4.6 common
mv build-0.4.6 build
mv survival-0.4.6 survival
popd

# Shows empty spaces with current font, must be re-checked in 0.4.8+
rm %{buildroot}%{_datadir}/%{name}/locale/ru/LC_MESSAGES/minetest.mo


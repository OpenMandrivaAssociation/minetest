%define gameversion 0.4.4

Name:		minetest
Version:	0.4.4
Release:	1
Summary:	An InfiniMiner/Minecraft inspired game
Group:		Games/Other
License:	GPLv2+
URL:		http://celeron.55.lt/minetest/
# Get from github and re-pack to get rid of ugly directory names
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}_game-%{gameversion}.tar.bz2
# Needed to fix build against jthread 1.3.1
Patch0:		minetest-0.4.4-jthread.patch
BuildRequires:	cmake >= 2.6.0
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	irrlicht-devel
BuildRequires:	jpeg-devel
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(jthread)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	pkgconfig(x11)

%description
One of the first InfiniMiner/Minecraft(/whatever) inspired games (started
October 2010), with a goal of taking the survival multiplayer gameplay
to a slightly different direction.

This game is under development, and as of now, the game does not really
differ from Minecraft except for having a lot less features. Still, playing
is quite fun already, especially for people who have not been able to
experience Minecraft.

%prep
%setup -q -a 1
%patch0 -p1

%build
%cmake -DJTHREAD_INCLUDE_DIR=%{_includedir}/jthread -DENABLE_GETTEXT:BOOL=ON
%make

%install
%makeinstall_std -C build

mkdir -p %{buildroot}%{_datadir}/%{name}/games/%{name}_game
cp -r %{name}_game-%{gameversion}/* %{buildroot}%{_datadir}/%{name}/games/%{name}_game

%find_lang %{name}

%files -f %{name}.lang
%doc doc/*.txt
%{_bindir}/%{name}
%{_bindir}/%{name}server
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}-icon.svg
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}server.6*



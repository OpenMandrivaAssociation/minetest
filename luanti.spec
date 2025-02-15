# BIG FAT WARNING #
# minetest_game != (it's not the same) as minetest or luanti. It is a separate project that should be packaged separate.
# luanti (and previous minetest) is game engine only.
# while minetest_game (and maybe in future luanti-game) is only game.

Summary:	An InfiniMiner/Minecraft inspired game
Name:		minetest_game
Version:	5.8.0
Release:	1
License:	GPLv2+
Group:		Games
Url:		https://luanti.org

Source0:	https://github.com/luanti-org/minetest_game/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:  luanti
# renamed from minetest
Obsoletes: minetest < %{version}

%description
One of the first InfiniMiner/Minecraft(/whatever) inspired games (started
October 2010), with a goal of taking the survival multiplayer gameplay
to a slightly different direction.

This game is under development, and as of now, the game does not really
differ from Minecraft except for having a lot less features. Still, playing
is quite fun already, especially for people who have not been able to
experience Minecraft.


%files
%license LICENSE.txt
%doc README.md
%dir %{_datadir}/minetest/
%dir %{_datadir}/minetest/games/
%{_datadir}/minetest/games/minetest_game/
#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n minetest_game-%{version}

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/minetest/games/minetest_game
cp -ar * %{buildroot}%{_datadir}/minetest/games/minetest_game

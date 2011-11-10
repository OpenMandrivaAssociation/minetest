Name:		minetest
Version:	0.3.1
Release:	%mkrel 1
Summary:	An InfiniMiner/Minecraft inspired game
Group:		Games/Other
License:	GPLv2+
URL:		http://celeron.55.lt/minetest/
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
BuildRequires:	cmake >= 2.6.0
BuildRequires:	irrlicht-devel
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	jpeg-devel
BuildRequires:	libx11-devel
BuildRequires:	libjthread-devel
BuildRequires:	sqlite3-devel
BuildRequires:	gettext-devel
BuildRequires:	desktop-file-utils

%description
One of the first InfiniMiner/Minecraft(/whatever) inspired games (started
October 2010), with a goal of taking the survival multiplayer gameplay
to a slightly different direction.

This game is under development, and as of now, the game does not really
differ from Minecraft except for having a lot less features. Still, playing
is quite fun already, especially for people who have not been able to
experience Minecraft.

Warning! For 0.3.1 the game still has no sound.

%prep
%setup -q

%build
%cmake -DJTHREAD_INCLUDE_DIR=%{_includedir}/jthread
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std
cd ..

mkdir -p %{buildroot}%{_iconsdir}/hicolor/scalable/apps
cp %{name}-icon.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc doc/*.txt
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/%{name}server
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}-icon.svg

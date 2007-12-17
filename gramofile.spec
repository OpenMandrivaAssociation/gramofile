%define name gramofile
%define version 1.6
%define release %mkrel 10

Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Sound
URL: http://panic.et.tudelft.nl/~costar/gramofile/
Source: %{name}-%{version}.tar.bz2
Patch0: tappin3a.patch.bz2
Patch1: tappin3b.patch.bz2
Patch2: gramofile-braille-patch.bz2
Summary: Transfer sound from gramophone records to CD
BuildRequires: libncurses-devel
BuildRequires: fftw2-devel

%description
GramoFile enables you to record audio from (for example) gramophone
records, process the signal and listen to the results. Because sound
files in .WAV-format are used, it is possible to exchange the files
with many other programs. Cdrecord(1) can burn CD-Recordables of these,
so you can make CDs with the music of your favorite records.  The user
interface of GramoFile has a windows-like look-and-feel, making it
fairly easy to use.

One of the most important parts of GramoFile is the ability to process
digital audio signals. Through the application of several filters it
is possible to accomplish a significant reduction of disturbances like
ticks and scratches. These filters have been programmed in such a fashion
that they can be applied in any order (and multiple times) in a single
run, thus avoiding the use of temporary files. It is possible to adjust
the properties of each filter independently, so in every situation an
optimal result can be achieved.

Another interesting feature is the track splitting. Just make one .wav
file of an entire side of an record and GramoFile will detect where
the individual tracks are located. This happens fully automatically,
without need to set any options. More experienced users may fine-tune
the algorithm, or change the detected track starts and ends, but
generally that will not be necessary. Track-times are saved in an
editable (plaintext) .tracks file, that will be used during the signal
processing to produce one processed .wav file for each individual track.

To record and play .wav files, modified versions of brec(1) and bplay(1)
by David Monro are included. These programs provide buffered recording
and playback, so all will go well even on a highly loaded system. Both
programs have been modified to support the standard GramoFile user
interface.  Brec also got a `graphical' peak level meter, and bplay a
running time display.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -pr bplay_gramo brec_gramo gramofile $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO ChangeLog *.txt example.tracks
%{_bindir}/*


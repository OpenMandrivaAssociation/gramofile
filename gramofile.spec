%define name gramofile
%define version 1.6
%define release 15

Name: %{name}
Version: %{version}
Release: %{release}
License: GPL+
Group: Sound
URL: http://www.opensourcepartners.nl/~costar/gramofile/
Source: %{name}-%{version}.tar.bz2
Patch0: tappin3a.patch.bz2
Patch1: tappin3b.patch.bz2
Patch2: gramofile-braille-patch.bz2
Summary: Transfer sound from gramophone records to CD
BuildRequires: ncurses-devel
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



%changelog
* Sun Jun 21 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 1.6-13mdv2010.0
+ Revision: 387540
- fix URL
- fix license tag

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.6-12mdv2009.0
+ Revision: 246609
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.6-10mdv2008.1
+ Revision: 126265
- kill re-definition of %%buildroot on Pixel's request
- import gramofile


* Thu Feb 02 2005 Lenny Cartier <lenny@mandriva.com> 1.6-10mdk
- rebuild

* Sun Nov 14 2004 Götz Waschk <waschk@linux-mandrake.com> 1.6-9mdk
- fix buildrequires

* Fri Oct 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.6-8mdk
- fix buildrequires

* Wed Apr 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.6-7mdk
- add Patch0: corrects some negative overflow checking in CMF-2 
- add Patch1: adds the updated CMF-3 filter to GramoFile 1.6
- add Patch2: gramofile-braille-patch

* Tue Mar 11 2003 Götz Waschk <waschk@linux-mandrake.com> 1.6-6mdk
- fix buildrequires

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.6-5mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.6-4mdk
- rebuild

* Tue Jul 24 2001  Lenny Cartier <lenny@mandrakesoft.com> 1.6-3mdk
- rebuild

* Wed Jan 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.6-2mdk
- rebuild
- add url

* Thu Oct 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.6-1mdk
- used srpm from Götz Wasch :
	Wed Oct  4 2000 Götz Waschk <waschk@linux-mandrake.com> 1.6-1mdk
	- initial Mandrake build


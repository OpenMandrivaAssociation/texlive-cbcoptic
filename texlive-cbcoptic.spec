Name:		texlive-cbcoptic
Version:	16666
Release:	2
Summary:	Coptic fonts and LaTeX macros for general usage and for philology
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/coptic/cbcoptic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cbcoptic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cbcoptic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
CBcoptic is a bundle of files for typesetting Coptic
philological text with the proper fonts and hyphenation. The
fonts are based on, but much extend, the fonts of the original
coptic bundle. The CBcoptic bundle includes font description
files, MetaFont sources and equivalent Adobe Type 1 fonts in
pfb format. The bundle also includes a package that provides
some macros of philological interest.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/cbcoptic/coptbase.mf
%{_texmfdistdir}/fonts/source/public/cbcoptic/copti.mf
%{_texmfdistdir}/fonts/source/public/cbcoptic/copto.mf
%{_texmfdistdir}/fonts/tfm/public/cbcoptic/copti.tfm
%{_texmfdistdir}/fonts/tfm/public/cbcoptic/copto.tfm
%{_texmfdistdir}/fonts/type1/public/cbcoptic/copti.pfb
%{_texmfdistdir}/fonts/type1/public/cbcoptic/copto.pfb
%{_texmfdistdir}/tex/latex/cbcoptic/coptic.sty
%{_texmfdistdir}/tex/latex/cbcoptic/lcopcoptic.fd
%{_texmfdistdir}/tex/latex/cbcoptic/prnthyph.sty
%doc %{_texmfdistdir}/doc/latex/cbcoptic/README
%doc %{_texmfdistdir}/doc/latex/cbcoptic/coptfont.pdf
%doc %{_texmfdistdir}/doc/latex/cbcoptic/testcop.tex
%doc %{_texmfdistdir}/doc/latex/cbcoptic/testcopOK.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}

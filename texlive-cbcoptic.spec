# revision 16666
# category Package
# catalog-ctan /language/coptic/cbcoptic
# catalog-date 2010-01-11 08:55:42 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-cbcoptic
Version:	0.2
Release:	1
Summary:	Coptic fonts and LaTeX macros for general usage and for philology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/coptic/cbcoptic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cbcoptic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cbcoptic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
CBcoptic is a bundle of files for typesetting Coptic
philological text with the proper fonts and hyphenation. The
fonts are based on, but much extend, the fonts of the original
coptic bundle. The CBcoptic bundle includes font description
files, MetaFont sources and equivalent Adobe Type 1 fonts in
pfb format. The bundle also includes a package that provides
some macros of philological interest.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

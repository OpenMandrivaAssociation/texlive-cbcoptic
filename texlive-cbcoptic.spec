%global tl_name cbcoptic
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Coptic fonts and LaTeX macros for general usage and for philology
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/coptic/cbcoptic
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cbcoptic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cbcoptic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
CBcoptic is a bundle of files for typesetting Coptic philological text
with the proper fonts and hyphenation. The fonts are based on, but much
extend, the fonts of the original coptic bundle. The CBcoptic bundle
includes font description files, Metafont sources and equivalent Adobe
Type 1 fonts in pfb format. The bundle also includes a package that
provides some macros of philological interest.


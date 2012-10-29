# revision 27721
# category Package
# catalog-ctan /macros/latex/contrib/ledmac
# catalog-date 2012-09-17 12:04:36 +0200
# catalog-license lppl
# catalog-version 0.19
Name:		texlive-ledmac
Version:	0.19
Release:	1
Summary:	Typeset scholarly editions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ledmac
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ledmac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ledmac.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ledmac.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A macro package for typesetting scholarly critical editions.
The ledmac package is a LaTeX port of the plain TeX EDMAC
macros. It supports indexing by page and line number and simple
tabular- and array-style environments. The package is
distributed with the related ledpar and ledarab packages. The
package is now superseded by eledmac.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ledmac/afoot.sty
%{_texmfdistdir}/tex/latex/ledmac/ledarab.sty
%{_texmfdistdir}/tex/latex/ledmac/ledmac.sty
%{_texmfdistdir}/tex/latex/ledmac/ledpar.sty
%doc %{_texmfdistdir}/doc/latex/ledmac/Makefile
%doc %{_texmfdistdir}/doc/latex/ledmac/README
%doc %{_texmfdistdir}/doc/latex/ledmac/djd17nov.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/djd17novL.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/djd17novR.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/djdpoems.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/djdpoems1.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/djdpoems2.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/djdpoems3.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/djdpoems4.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/egarab.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/egarab.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/egarabpar.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/egarabpar.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/ledarab.pdf
%doc %{_texmfdistdir}/doc/latex/ledmac/ledarden.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/ledarden.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/ledbraonain.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/ledbraonain.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/ledeasy.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/ledeasy.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/ledekker.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/ledekker.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/ledfeat.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/ledfeat.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/ledioc.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/ledioc.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/ledmac.pdf
%doc %{_texmfdistdir}/doc/latex/ledmac/ledmixed.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/ledmixed.tex
%doc %{_texmfdistdir}/doc/latex/ledmac/ledpar.pdf
%doc %{_texmfdistdir}/doc/latex/ledmac/villon.eps
%doc %{_texmfdistdir}/doc/latex/ledmac/villon.tex
#- source
%doc %{_texmfdistdir}/source/latex/ledmac/ledarab.dtx
%doc %{_texmfdistdir}/source/latex/ledmac/ledarab.ins
%doc %{_texmfdistdir}/source/latex/ledmac/ledmac.dtx
%doc %{_texmfdistdir}/source/latex/ledmac/ledmac.ins
%doc %{_texmfdistdir}/source/latex/ledmac/ledpar.dtx
%doc %{_texmfdistdir}/source/latex/ledmac/ledpar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

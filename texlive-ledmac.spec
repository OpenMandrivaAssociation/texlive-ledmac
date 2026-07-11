%global tl_name ledmac
%global tl_revision 41811

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.19.4
Release:	%{tl_revision}.1
Summary:	Typeset scholarly editions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ledmac
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ledmac.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ledmac.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ledmac.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A macro package for typesetting scholarly critical editions. The ledmac
package is a LaTeX port of the plain TeX EDMAC macros. It supports
indexing by page and line number and simple tabular- and array-style
environments. The package is distributed with the related ledpar and
ledarab packages. The package is now superseded by reledmac.


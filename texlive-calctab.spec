# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/calctab
# catalog-date 2009-07-14 21:55:02 +0200
# catalog-license lppl
# catalog-version v0.6.1
Name:		texlive-calctab
Version:	v0.6.1
Release:	1
Summary:	Language for numeric tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/calctab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calctab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calctab.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The calctab package helps the user to typeset a kind of
economic table such as invoices, expense notes and liquidation,
or other tabular material with a values column. The code
computes sum and percentage with floating point numeric methods
(using the fltpoint package) and builds the render table task.

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
%{_texmfdistdir}/tex/latex/calctab/calctab.sty
%doc %{_texmfdistdir}/doc/latex/calctab/README
%doc %{_texmfdistdir}/doc/latex/calctab/calctab_manual.pdf
%doc %{_texmfdistdir}/doc/latex/calctab/calctab_manual.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

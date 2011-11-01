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
Requires(post):	texlive-tlpkg
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
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/calctab/calctab.sty
%doc %{_texmfdistdir}/doc/latex/calctab/README
%doc %{_texmfdistdir}/doc/latex/calctab/calctab_manual.pdf
%doc %{_texmfdistdir}/doc/latex/calctab/calctab_manual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

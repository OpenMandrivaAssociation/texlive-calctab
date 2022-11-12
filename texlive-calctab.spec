Name:		texlive-calctab
Version:	15878
Release:	1
Summary:	Language for numeric tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/calctab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calctab.r15878.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calctab.doc.r15878.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The calctab package helps the user to typeset a kind of
economic table such as invoices, expense notes and liquidation,
or other tabular material with a values column. The code
computes sum and percentage with floating point numeric methods
(using the fltpoint package) and builds the render table task.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/calctab/calctab.sty
%doc %{_texmfdistdir}/doc/latex/calctab/README
%doc %{_texmfdistdir}/doc/latex/calctab/calctab_manual.pdf
%doc %{_texmfdistdir}/doc/latex/calctab/calctab_manual.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

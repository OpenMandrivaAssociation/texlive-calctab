# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/calctab
# catalog-date 2009-07-14 21:55:02 +0200
# catalog-license lppl
# catalog-version v0.6.1
Name:		texlive-calctab
Version:	0.6.1
Release:	2
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.6.1-2
+ Revision: 749950
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.6.1-1
+ Revision: 717994
- texlive-calctab
- texlive-calctab
- texlive-calctab
- texlive-calctab
- texlive-calctab


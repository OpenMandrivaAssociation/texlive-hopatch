Name:		texlive-hopatch
Version:	65491
Release:	1
Summary:	Load patches for packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hopatch
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hopatch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hopatch.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hopatch.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Hopatch provides a command with which the user may register of
patch code for a particular package. Hopatch will apply the
patch immediately, if the relevant package has already been
loaded; otherwise it will store the patch until the package
appears.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hopatch
%{_texmfdistdir}/tex/latex/hopatch
%doc %{_texmfdistdir}/doc/latex/hopatch

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

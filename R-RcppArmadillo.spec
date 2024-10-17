%global packname RcppArmadillo
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3.900.0
Release:          1
Summary:          Rcpp integration for Armadillo templated linear algebra library
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3.900.0.tar.gz
Requires:         R-Rcpp >= 0.10.2 R-inline R-RUnit
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-Rcpp >= 0.10.2 R-inline R-RUnit
BuildRequires:    liblapack-devel

%description
R and Armadillo integration using Rcpp Armadillo is a
templated C++ linear algebra library (by Conrad Sanderson) that
aims towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported, as
well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time) to
combine several operations into one, and to reduce (or
eliminate) the need for temporaries. This is accomplished
through recursive templates and template meta-programming.
This library is useful if C++ has been decided as the language of
choice (due to speed and/or integration capabilities), rather than 
another language.
The RcppArmadillo package includes the header files from the templated
Armadillo library (currently version 3.820). Thus users do not
need to install Armadillo itself in order to use RcppArmadillo.
This Armadillo integration provides a nice illustration of the
capabilities of the Rcpp package for seamless R and C++ integration.
Armadillo is licensed under the MPL 2.0, while RcppArmadillo (the Rcpp
bindings/bridge to Armadillo) is licensed under the GNU GPL
version 2 or later, as is the rest of Rcpp.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/announce
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/skeleton
%{rlibdir}/%{packname}/unitTests

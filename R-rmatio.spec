#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rmatio
Version  : 0.14.0
Release  : 12
URL      : https://cran.r-project.org/src/contrib/rmatio_0.14.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rmatio_0.14.0.tar.gz
Summary  : Read and Write 'Matlab' Files
Group    : Development/Tools
License  : BSD-2-Clause GPL-3.0
Requires: R-rmatio-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : pkgconfig(zlib)

%description
package supports reading MAT version 4, MAT version 5 and MAT
    compressed version 5. The 'rmatio' package can write version 5 MAT
    files and version 5 files with variable compression.

%package lib
Summary: lib components for the R-rmatio package.
Group: Libraries

%description lib
lib components for the R-rmatio package.


%prep
%setup -q -c -n rmatio
cd %{_builddir}/rmatio

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589538883

%install
export SOURCE_DATE_EPOCH=1589538883
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmatio
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmatio
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmatio
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rmatio || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rmatio/DESCRIPTION
/usr/lib64/R/library/rmatio/INDEX
/usr/lib64/R/library/rmatio/Meta/Rd.rds
/usr/lib64/R/library/rmatio/Meta/features.rds
/usr/lib64/R/library/rmatio/Meta/hsearch.rds
/usr/lib64/R/library/rmatio/Meta/links.rds
/usr/lib64/R/library/rmatio/Meta/nsInfo.rds
/usr/lib64/R/library/rmatio/Meta/package.rds
/usr/lib64/R/library/rmatio/NAMESPACE
/usr/lib64/R/library/rmatio/NEWS
/usr/lib64/R/library/rmatio/NOTICE
/usr/lib64/R/library/rmatio/R/rmatio
/usr/lib64/R/library/rmatio/R/rmatio.rdb
/usr/lib64/R/library/rmatio/R/rmatio.rdx
/usr/lib64/R/library/rmatio/extdata/OneOnly.mat
/usr/lib64/R/library/rmatio/extdata/matio_test_cases_compressed_le.mat
/usr/lib64/R/library/rmatio/extdata/matio_test_cases_v4_be.mat
/usr/lib64/R/library/rmatio/extdata/matio_test_cases_v4_le.mat
/usr/lib64/R/library/rmatio/extdata/small_v4_be.mat
/usr/lib64/R/library/rmatio/extdata/small_v4_le.mat
/usr/lib64/R/library/rmatio/help/AnIndex
/usr/lib64/R/library/rmatio/help/aliases.rds
/usr/lib64/R/library/rmatio/help/paths.rds
/usr/lib64/R/library/rmatio/help/rmatio.rdb
/usr/lib64/R/library/rmatio/help/rmatio.rdx
/usr/lib64/R/library/rmatio/html/00Index.html
/usr/lib64/R/library/rmatio/html/R.css
/usr/lib64/R/library/rmatio/tests/arguments.R
/usr/lib64/R/library/rmatio/tests/array.R
/usr/lib64/R/library/rmatio/tests/cell.R
/usr/lib64/R/library/rmatio/tests/complex.R
/usr/lib64/R/library/rmatio/tests/dgCMatrix.R
/usr/lib64/R/library/rmatio/tests/lists.R
/usr/lib64/R/library/rmatio/tests/logical.R
/usr/lib64/R/library/rmatio/tests/matio_test_datasets.R
/usr/lib64/R/library/rmatio/tests/matrix.R
/usr/lib64/R/library/rmatio/tests/one_only.R
/usr/lib64/R/library/rmatio/tests/string.R
/usr/lib64/R/library/rmatio/tests/structure.R
/usr/lib64/R/library/rmatio/tests/vector.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rmatio/libs/rmatio.so
/usr/lib64/R/library/rmatio/libs/rmatio.so.avx2
/usr/lib64/R/library/rmatio/libs/rmatio.so.avx512

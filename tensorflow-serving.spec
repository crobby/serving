%define _disable_source_fetch 0
%define _rpmfilename %%{ARCH}/tensorflow_model_server-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm
Name: tensorflow_model_server
Version: 1.6.0
Release: 1%{?dist}
Summary: RPM for tensorflow-serving package

License: ASL 2.0
URL: https://github.com/tensorflow/serving
Source0: https://github.com/tensorflow/serving/archive/1.6.0.tar.gz

BuildRequires: bazel < 0.12
BuildRequires: python-devel
BuildRequires: numpy
BuildRequires: gcc-c++

%description

%global debug_package %{nil}
%prep
%setup -n serving-%{version}

%build
bazel build -c opt //tensorflow_serving/model_servers:tensorflow_model_server

%install
mkdir -p %{buildroot}%{_bindir}
cp ./bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server %{buildroot}%{_bindir}

%files
%{_bindir}/tensorflow_model_server

%changelog
* Thu Apr 26 2018 Chad Roberts <croberts@redhat.com>
Initial version
- 

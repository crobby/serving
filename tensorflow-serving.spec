%define _disable_source_fetch 0
Name: serving
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


%prep
%autosetup

%build
bazel build -c opt //tensorflow_serving/model_servers:tensorflow_model_server

%install
mkdir -p %{buildroot}%{_bindir}
cp ./bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server %{buildroot}%{_bindir}
rm -rf $RPM_BUILD_ROOT

%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Thu Apr 26 2018 Chad Roberts <croberts@redhat.com>
Initial version
- 

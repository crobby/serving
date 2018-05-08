%define _disable_source_fetch 0
Name: tensorflow-model-server-gpu
Version: 1.6.0
Release: 1%{?dist}
Summary: RPM for tensorflow-serving GPU package

License: ASL 2.0
URL: https://github.com/tensorflow/serving
Source0: https://github.com/tensorflow/serving/archive/1.6.0.tar.gz

BuildRequires: bazel < 0.12
BuildRequires: python-devel
BuildRequires: gcc-c++
BuildRequires: mock
BuildRequires: numpy
BuildRequires: cuda < 9

%description

%global debug_package %{nil}
%prep
%setup -n serving-%{version}

%build
export LD_LIBRARY_PATH=/opt/rh/python27/root/usr/lib64:/usr/local/cuda/lib64
export BAZELRC=/root/.bazelrc
export TF_SERVING_VERSION=tags/1.6.0
export TF_CUDA_VERSION=8.0
export TF_CUDNN_VERSION=6
export BAZEL_VERSION=0.5.4
export TF_NEED_CUDA=1
export TF_NEED_S3=0
export TF_CUDA_COMPUTE_CAPABILITIES="3.5,5.2,6.1"
export TF_NEED_GCP=1
export TF_NEED_JEMALLOC=0
export TF_NEED_HDFS=1
export TF_NEED_OPENCL=0
export TF_NEED_MKL=0
export TF_NEED_VERBS=0
export TF_NEED_MPI=0
export TF_NEED_GDR=0
export TF_ENABLE_XLA=1
export TF_CUDA_CLANG=0
export TF_NEED_OPENCL_SYCL=0
export CUDA_TOOLKIT_PATH=/usr/local/cuda
export CUDNN_INSTALL_PATH=/usr/local/cuda
export GCC_HOST_COMPILER_PATH=/usr/bin/gcc
export PYTHON_BIN_PATH=/usr/bin/python
export CC_OPT_FLAGS="-march=native"
export PYTHON_LIB_PATH=/usr/lib64/python2.7/site-packages

bazel build -c opt --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-mfpmath=both --copt=-msse4.2 --config=cuda -k --verbose_failures --crosstool_top=@local_config_cuda//crosstool:toolchain tensorflow_serving/model_servers:tensorflow_model_server

%install
mkdir -p %{buildroot}%{_bindir}
cp ./bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server %{buildroot}%{_bindir}

%files
%{_bindir}/tensorflow_model_server

%changelog
* Mon Apr 30 2018 Chad Roberts <croberts@redhat.com>
Initial version
- 
